#!/bin/bash
# construire-iso.sh : fabrique l'ISO Occitux à partir de l'ISO officielle PrimTux.
#
#   sudo ./construire/construire-iso.sh <PrimTux.iso> <occitux_x.y.z_all.deb> [sortie.iso]
#
# OCCITUX_LANGUE=bearnes|oc|fr choisit la langue par défaut des PC installés
# depuis cette ISO (par défaut : celle du paquet, oc). En béarnais, les menus
# de démarrage viennent de traductions/occitux.csv.
#
# On ouvre le système de l'ISO (casper/filesystem.squashfs), on y installe le
# paquet occitux, on le referme, et xorriso recopie l'ISO d'origine en ne
# remplaçant que les fichiers modifiés : le démarrage BIOS et UEFI de PrimTux
# est conservé tel quel.
set -euo pipefail

ICI=$(cd "$(dirname "$0")" && pwd)
SOURCES="$ICI/sources-primtux.txt"

die() { echo "construire-iso : $*" >&2; exit 1; }

[ $# -ge 2 ] || die "usage : sudo $0 <PrimTux.iso> <occitux.deb> [sortie.iso]"
ISO=$(realpath "$1")
DEB=$(realpath "$2")
VERSION=$(dpkg-deb -f "$DEB" Version)
SORTIE=$(realpath -m "${3:-occitux-${VERSION}.iso}")

LANGUE=${OCCITUX_LANGUE:-}
case "$LANGUE" in
    ''|bearnes|oc|fr) ;;
    *) die "OCCITUX_LANGUE=$LANGUE inconnue (bearnes, oc ou fr)" ;;
esac

# Texte béarnais d'une clé de traductions/occitux.csv (clau;frances;bearnes),
# ou le texte français donné en second argument.
TEXTES="$ICI/../traductions/occitux.csv"
texte() {
    local cle=$1 francais=$2 bearnes=
    if [ "$LANGUE" = bearnes ] && [ -f "$TEXTES" ]; then
        bearnes=$(awk -F';' -v c="$cle" '$1 == c { print $3 }' "$TEXTES")
    fi
    echo "${bearnes:-$francais}"
}
ESSAYER=$(texte demarrage.essayer "Essayer Occitux")
INSTALLER=$(texte demarrage.installer "Installer Occitux")

[ "$(id -u)" -eq 0 ] || die "à lancer avec sudo (montages et chroot)"
[ -f "$ISO" ] || die "ISO introuvable : $ISO"
[ -f "$DEB" ] || die "paquet introuvable : $DEB"
for outil in xorriso unsquashfs mksquashfs sha256sum; do
    command -v "$outil" >/dev/null || die "outil manquant : $outil (sudo apt install xorriso squashfs-tools)"
done

# 1. L'ISO doit être une version de PrimTux connue et intacte.
nom=$(basename "$ISO")
attendu=$(awk -v n="$nom" '$1 == n { print $2 }' "$SOURCES")
[ -n "$attendu" ] || die "$nom n'est pas dans $SOURCES : ajouter sa somme SHA-256 après l'avoir vérifiée"
echo "Vérification de $nom..."
echo "$attendu  $ISO" | sha256sum --check --status || die "somme SHA-256 incorrecte pour $nom"

TRAVAIL=$(mktemp -d "${TMPDIR:-/var/tmp}/occitux.XXXXXX")
RACINE="$TRAVAIL/racine"
MONTAGES=()

# Arrête les processus restés dans le système (le menu PrimTux en lance un
# à chaque installation de paquet), sinon /dev/pts refuse de se démonter.
arreter_processus_chroot() {
    local signal p
    for signal in TERM KILL; do
        for p in /proc/[0-9]*; do
            if [ "$(readlink "$p/root" 2>/dev/null)" = "$RACINE" ]; then
                kill "-$signal" "${p#/proc/}" 2>/dev/null || true
            fi
        done
        sleep 2
    done
    return 0
}

nettoyer() {
    local i
    arreter_processus_chroot
    for ((i = ${#MONTAGES[@]} - 1; i >= 0; i--)); do
        umount -l "${MONTAGES[i]}" 2>/dev/null || true
    done
    rm -rf "$TRAVAIL"
}
trap nettoyer EXIT

# 2. Extraction du système.
echo "Extraction du système (plusieurs minutes)..."
xorriso -osirrox on -indev "$ISO" \
    -extract /casper/filesystem.squashfs "$TRAVAIL/filesystem.squashfs" 2>/dev/null \
    || die "pas de /casper/filesystem.squashfs dans l'ISO : est-ce bien une PrimTux basée sur Mint ?"
# md5sum.txt sert au contrôle d'intégrité du menu de démarrage ; facultatif.
xorriso -osirrox on -indev "$ISO" -extract /md5sum.txt "$TRAVAIL/md5sum.txt" >/dev/null 2>&1 || true
COMPRESSION=$(unsquashfs -s "$TRAVAIL/filesystem.squashfs" | awk '/^Compression/ { print $2 }')
unsquashfs -q -d "$RACINE" "$TRAVAIL/filesystem.squashfs"
rm "$TRAVAIL/filesystem.squashfs"

# 3. Installation du paquet dans le système, sans lancer de service.
for m in dev dev/pts proc sys run; do
    mount --bind "/$m" "$RACINE/$m"
    MONTAGES+=("$RACINE/$m")
done
mv "$RACINE/etc/resolv.conf" "$TRAVAIL/resolv.conf.origine"
cp -L /etc/resolv.conf "$RACINE/etc/resolv.conf"
printf '#!/bin/sh\nexit 101\n' > "$RACINE/usr/sbin/policy-rc.d"
chmod 755 "$RACINE/usr/sbin/policy-rc.d"
cp "$DEB" "$RACINE/tmp/occitux.deb"

echo "Installation de occitux $VERSION dans le système..."
chroot "$RACINE" /usr/bin/env DEBIAN_FRONTEND=noninteractive LC_ALL=C.UTF-8 sh -c '
    apt-get update -q &&
    apt-get install -y -q /tmp/occitux.deb &&
    apt-get clean
'
if [ -n "$LANGUE" ]; then
    echo "Langue par défaut : $LANGUE"
    sed -i "s/^LANGUE=.*/LANGUE=$LANGUE/" "$RACINE/etc/occitux/occitux.conf"
    chroot "$RACINE" /usr/bin/env LC_ALL=C.UTF-8 occitux-config
fi

rm -f "$RACINE/tmp/occitux.deb" "$RACINE/usr/sbin/policy-rc.d"
rm -f "$RACINE/etc/resolv.conf"
mv "$TRAVAIL/resolv.conf.origine" "$RACINE/etc/resolv.conf"
# shellcheck disable=SC2016 # format de dpkg-query, pas une variable du shell
chroot "$RACINE" dpkg-query -W --showformat='${Package} ${Version}\n' > "$TRAVAIL/filesystem.manifest"
arreter_processus_chroot
for ((i = ${#MONTAGES[@]} - 1; i >= 0; i--)); do umount "${MONTAGES[i]}"; done
MONTAGES=()

# 4. Fermeture du système, avec la compression d'origine.
echo "Compression du système ($COMPRESSION, plusieurs minutes)..."
du -sx --block-size=1 "$RACINE" | cut -f1 > "$TRAVAIL/filesystem.size"
mksquashfs "$RACINE" "$TRAVAIL/filesystem.squashfs" -comp "$COMPRESSION" -noappend -quiet

REMPLACER=(
    -map "$TRAVAIL/filesystem.squashfs" /casper/filesystem.squashfs
    -map "$TRAVAIL/filesystem.manifest" /casper/filesystem.manifest
    -map "$TRAVAIL/filesystem.size" /casper/filesystem.size
)

# Entrée « Tester la mémoire » : memtest86+ est sur l'ISO de PrimTux, mais
# absent de ses menus. Sur les PC reconditionnés, une barrette défectueuse ou
# mal assortie fait planter le noyau dès son démarrage (kernel panic dans
# l'allocateur de mémoire), un message qui ne fait pas penser à la mémoire.
ajouter_test_memoire() {
    local menu=$1 copie=$2
    case "$menu" in
        /boot/grub/grub.cfg)
            xorriso -indev "$ISO" -ls /boot/memtest64.efi >/dev/null 2>&1 || return 0
            cat >> "$copie" <<'EOF'

menuentry "Tester la mémoire" {
	linux	/boot/memtest64.efi
}
EOF
            ;;
        /isolinux/menu.cfg)
            xorriso -indev "$ISO" -ls /boot/memtest64.bin >/dev/null 2>&1 || return 0
            sed -i 's|^menu clear$|label memtest\n  menu label Tester la memoire\n  linux /boot/memtest64.bin\n\nmenu clear|' "$copie"
            ;;
    esac
}

# Menus de démarrage UEFI (GRUB) et BIOS (isolinux) : « Occitux » à la place
# de « PrimTux » dans les seuls textes affichés, jamais dans les chemins.
mkdir -p "$TRAVAIL/menus"
for menu in /boot/grub/grub.cfg /boot/grub/live-theme/theme.txt \
            /isolinux/menu.cfg /isolinux/live.cfg /isolinux/install.cfg; do
    copie="$TRAVAIL/menus/$(echo "${menu#/}" | tr / _)"
    xorriso -osirrox on -indev "$ISO" -extract "$menu" "$copie" >/dev/null 2>&1 || continue
    chmod u+w "$copie"
    sed -i -e 's/^\(menuentry "[^"]*\)PrimTux"/\1Occitux"/' \
           -e 's/^\(\s*menu \(label\|title\) .*\)PrimTux$/\1Occitux/' \
           -e 's/^title-text: "PrimTux"$/title-text: "Occitux"/' \
           -e "s/^\(menuentry \"\|\s*menu label \)Essayer Occitux/\1$ESSAYER/" \
           -e "s/^\(menuentry \"\|\s*menu label \)Installer Occitux/\1$INSTALLER/" "$copie"
    # grub.cfg de PrimTux 9 se termine par un « EOF » oublié, que GRUB lit
    # comme une commande inconnue.
    [ "$menu" = /boot/grub/grub.cfg ] && sed -i '${/^EOF$/d}' "$copie"
    ajouter_test_memoire "$menu" "$copie"
    REMPLACER+=(-map "$copie" "$menu")
done
# Le contrôle d'intégrité du menu de démarrage lit md5sum.txt, s'il existe.
if [ -f "$TRAVAIL/md5sum.txt" ]; then
    for f in filesystem.squashfs filesystem.manifest filesystem.size; do
        somme=$(md5sum "$TRAVAIL/$f" | cut -d' ' -f1)
        sed -i "s|^[0-9a-f]\{32\}  \./casper/$f\$|$somme  ./casper/$f|" "$TRAVAIL/md5sum.txt"
    done
    REMPLACER+=(-map "$TRAVAIL/md5sum.txt" /md5sum.txt)
fi

# 5. Nouvelle ISO : copie de l'originale, fichiers modifiés remplacés.
echo "Écriture de $SORTIE..."
rm -f "$SORTIE"
xorriso -indev "$ISO" -outdev "$SORTIE" \
    -compliance iso_9660_level=3 \
    "${REMPLACER[@]}" \
    -boot_image any replay
(cd "$(dirname "$SORTIE")" && sha256sum "$(basename "$SORTIE")" > "$(basename "$SORTIE").sha256")

echo "Terminé : $SORTIE"
