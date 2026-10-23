#!/bin/bash
# construire-iso.sh : fabrique l'ISO Occitux à partir de l'ISO officielle PrimTux.
#
#   sudo ./construire/construire-iso.sh <PrimTux.iso> <occitux_x.y.z_all.deb> [sortie.iso]
#
# OCCITUX_LANGUE=oc|bearnes|fr : langue par défaut des PC installés depuis
#   cette ISO et de ses menus de démarrage (par défaut : oc).
# OCCITUX_INSTALLATION=automatique : ISO de déploiement. Sans rien toucher,
#   le PC démarré sur la clé installe Occitux tout seul après 20 secondes,
#   EN EFFAÇANT TOUT SON DISQUE, puis s'éteint. Sinon, l'installation
#   automatique reste une entrée du menu, et « Essayer » est l'entrée par défaut.
#
# On ouvre le système de l'ISO (casper/filesystem.squashfs), on y installe le
# paquet occitux, on le referme, et xorriso recopie l'ISO d'origine en ne
# remplaçant que les fichiers modifiés : le démarrage BIOS et UEFI de PrimTux
# est conservé tel quel.
set -euo pipefail

ICI=$(cd "$(dirname "$0")" && pwd)
SOURCES="$ICI/sources-primtux.txt"
PRESEED="$ICI/preseed"
TEXTES="$ICI/../traductions/occitux.csv"

die() { echo "construire-iso : $*" >&2; exit 1; }

[ $# -ge 2 ] || die "usage : sudo $0 <PrimTux.iso> <occitux.deb> [sortie.iso]"
ISO=$(realpath "$1")
DEB=$(realpath "$2")
VERSION=$(dpkg-deb -f "$DEB" Version)

LANGUE=${OCCITUX_LANGUE:-oc}
case "$LANGUE" in
    bearnes|oc|fr) ;;
    *) die "OCCITUX_LANGUE=$LANGUE inconnue (oc, bearnes ou fr)" ;;
esac
INSTALLATION=${OCCITUX_INSTALLATION:-menu}
case "$INSTALLATION" in
    menu|automatique) ;;
    *) die "OCCITUX_INSTALLATION=$INSTALLATION inconnue (menu ou automatique)" ;;
esac
suffixe=
[ "$INSTALLATION" = automatique ] && suffixe=-deploiement
SORTIE=$(realpath -m "${3:-occitux-${VERSION}${suffixe}.iso}")

# Texte d'une clé de traductions/occitux.csv (clau;frances;occitan;bearnes)
# dans la langue de l'ISO, ou le texte français donné en second argument.
texte() {
    local cle=$1 francais=$2 colonne traduit=
    case "$LANGUE" in bearnes) colonne=bearnes ;; oc) colonne=occitan ;; *) colonne= ;; esac
    if [ -n "$colonne" ] && [ -f "$TEXTES" ]; then
        traduit=$(awk -F';' -v c="$cle" -v col="$colonne" '
            NR == 1 { for (i = 1; i <= NF; i++) if ($i == col) n = i; next }
            $1 == c && n { print $n }' "$TEXTES")
    fi
    echo "${traduit:-$francais}"
}
# isolinux n'affiche pas les lettres accentuées : on les remplace.
sans_accents() { echo "$1" | iconv -f UTF-8 -t ASCII//TRANSLIT | tr -d "'^\`\"~"; }

ESSAYER=$(texte demarrage.essayer "Essayer Occitux")
INSTALLER=$(texte demarrage.installer "Installer Occitux")
INSTALLER_AUTO=$(texte demarrage.installer_auto "Installer Occitux automatiquement (efface tout le disque)")
MEMOIRE=$(texte demarrage.memoire "Tester la mémoire")
AVERTISSEMENT=$(texte demarrage.avertissement_auto "ATTENTION : dans 20 secondes, Occitux s'installe tout seul et efface tout le disque de ce PC. Pour l'éviter, retirez la clé et redémarrez.")

[ "$(id -u)" -eq 0 ] || die "à lancer avec sudo (montages et chroot)"
[ -f "$ISO" ] || die "ISO introuvable : $ISO"
[ -f "$DEB" ] || die "paquet introuvable : $DEB"
for f in occitux.seed choisir-disque.sh apres-installation.sh; do
    [ -f "$PRESEED/$f" ] || die "fichier manquant : $PRESEED/$f"
done
for outil in xorriso unsquashfs mksquashfs sha256sum iconv; do
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

# shellcheck disable=SC2317 # appelée par le trap EXIT
nettoyer() {
    local i
    arreter_processus_chroot
    for ((i = ${#MONTAGES[@]} - 1; i >= 0; i--)); do
        umount -l "${MONTAGES[i]}" 2>/dev/null || true
    done
    rm -rf "$TRAVAIL"
}
trap nettoyer EXIT

# Lit un fichier de l'ISO dans le dossier de travail ; échoue si absent.
extraire() {
    xorriso -osirrox on -indev "$ISO" -extract "$1" "$2" >/dev/null 2>&1 || return 1
    chmod u+w "$2"
}

# 2. Extraction du système.
echo "Extraction du système (plusieurs minutes)..."
extraire /casper/filesystem.squashfs "$TRAVAIL/filesystem.squashfs" \
    || die "pas de /casper/filesystem.squashfs dans l'ISO : est-ce bien une PrimTux basée sur Mint ?"
# md5sum.txt sert au contrôle d'intégrité du menu de démarrage ; facultatif.
extraire /md5sum.txt "$TRAVAIL/md5sum.txt" || true
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
echo "Langue par défaut : $LANGUE"
sed -i "s/^LANGUE=.*/LANGUE=$LANGUE/" "$RACINE/etc/occitux/occitux.conf"
chroot "$RACINE" /usr/bin/env LC_ALL=C.UTF-8 occitux-config
# Nom du PC de la session d'essai.
echo occitux > "$RACINE/etc/hostname"
sed -i 's/^\(127\.0\.1\.1\s\+\)primtux\b/\1occitux/' "$RACINE/etc/hosts"
# Message de fin (retirer la clé), en anglais dans casper : traduit sur la clé.
RETIRER=$(texte fin.retirer_cle "Retirez la clé USB, puis appuyez sur Entrée : ")
RETIRER_REDEMARRER=$(texte fin.retirer_cle_redemarrer "Retirez la clé USB, puis redémarrez.")
if [ -f "$RACINE/usr/sbin/casper-stop" ]; then
    sed -i -e "s|^\(\s*MSG=\)\"Please remove the installation medium, then press ENTER: \"|\1\"$RETIRER\"|" \
           -e "s|^\(\s*MSG_FALLBACK=\)\"Please remove the installation medium, then reboot.\"|\1\"$RETIRER_REDEMARRER\"|" \
           "$RACINE/usr/sbin/casper-stop"
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

# 5. Installation automatique : réponses de l'installateur et scripts.
mkdir -p "$TRAVAIL/preseed"
cp "$PRESEED/occitux.seed" "$PRESEED/choisir-disque.sh" "$PRESEED/apres-installation.sh" "$TRAVAIL/preseed/"
# Le preseed de PrimTux (sessions d'essai et installation classique), avec le
# nom de PC d'Occitux.
if extraire /preseed/ubuntu.seed "$TRAVAIL/preseed/ubuntu.seed"; then
    sed -i 's/^\(d-i netcfg\/get_hostname string \)primtux$/\1occitux/' "$TRAVAIL/preseed/ubuntu.seed"
    REMPLACER+=(-map "$TRAVAIL/preseed/ubuntu.seed" /preseed/ubuntu.seed)
fi
# Langue de l'installateur automatique : celle de l'ISO (Ubiquity est traduit
# en occitan par language-pack-oc, que le paquet occitux installe).
case "$LANGUE" in
    fr) LOCALE_INSTALLATEUR=fr_FR.UTF-8 ;;
    *)  LOCALE_INSTALLATEUR=oc_FR.UTF-8 ;;
esac
sed -i "s/^d-i debian-installer\/locale string .*/d-i debian-installer\/locale string $LOCALE_INSTALLATEUR/" "$TRAVAIL/preseed/occitux.seed"
for f in occitux.seed choisir-disque.sh apres-installation.sh; do
    REMPLACER+=(-map "$TRAVAIL/preseed/$f" "/preseed/$f")
done
# Paramètres noyau de l'installation automatique : ceux de PrimTux, le preseed
# d'Occitux, Ubiquity seul et sans question. Sans « noprompt » : à la fin,
# le PC demande de retirer la clé avant de s'éteindre, sinon il la
# redémarrerait et recommencerait l'installation.
PARAMS_AUTO="boot=casper fsck.mode=skip file=/cdrom/preseed/occitux.seed only-ubiquity automatic-ubiquity quiet splash ---"

# Entrée « Tester la mémoire » : memtest86+ est sur l'ISO de PrimTux, mais
# absent de ses menus. Sur les PC reconditionnés, une barrette défectueuse ou
# mal assortie fait planter le noyau dès son démarrage (kernel panic dans
# l'allocateur de mémoire), un message qui ne fait pas penser à la mémoire.
ajouter_test_memoire() {
    local menu=$1 copie=$2
    case "$menu" in
        /boot/grub/grub.cfg)
            xorriso -indev "$ISO" -ls /boot/memtest64.efi >/dev/null 2>&1 || return 0
            cat >> "$copie" <<FIN

menuentry "$MEMOIRE" {
	linux	/boot/memtest64.efi
}
FIN
            ;;
        /isolinux/menu.cfg)
            xorriso -indev "$ISO" -ls /boot/memtest64.bin >/dev/null 2>&1 || return 0
            sed -i "s|^menu clear\$|label memtest\n  menu label $(sans_accents "$MEMOIRE")\n  linux /boot/memtest64.bin\n\nmenu clear|" "$copie"
            ;;
    esac
}

# Entrée « Installer Occitux automatiquement » dans chaque menu.
ajouter_installation_auto() {
    local menu=$1 copie=$2
    case "$menu" in
        /boot/grub/grub.cfg)
            cat >> "$copie" <<FIN
menuentry "$INSTALLER_AUTO" {
	set gfxpayload=keep
	linux	/casper/vmlinuz $PARAMS_AUTO
	initrd	/casper/initrd.gz
}
FIN
            ;;
        /isolinux/install.cfg)
            cat >> "$copie" <<FIN
label installauto
  menu label $(sans_accents "$INSTALLER_AUTO")
  kernel /casper/vmlinuz
  append $PARAMS_AUTO initrd=/casper/initrd.gz
FIN
            ;;
    esac
}

# Menus de démarrage UEFI (GRUB) et BIOS (isolinux) : « Occitux » à la place
# de « PrimTux » dans les seuls textes affichés, jamais dans les chemins.
mkdir -p "$TRAVAIL/menus"
for menu in /boot/grub/grub.cfg /boot/grub/live-theme/theme.txt \
            /isolinux/isolinux.cfg /isolinux/menu.cfg /isolinux/live.cfg /isolinux/install.cfg; do
    copie="$TRAVAIL/menus/$(echo "${menu#/}" | tr / _)"
    extraire "$menu" "$copie" || continue
    sed -i -e 's/^\(menuentry "[^"]*\)PrimTux"/\1Occitux"/' \
           -e 's/^\(\s*menu \(label\|title\) .*\)PrimTux$/\1Occitux/' \
           -e 's/^title-text: "PrimTux"$/title-text: "Occitux"/' \
           -e "s/^\(menuentry \"\)Essayer Occitux/\1$ESSAYER/" \
           -e "s/^\(menuentry \"\)Installer Occitux/\1$INSTALLER/" \
           -e "s/^\(\s*menu label \)Essayer Occitux/\1$(sans_accents "$ESSAYER")/" \
           -e "s/^\(\s*menu label \)Installer Occitux/\1$(sans_accents "$INSTALLER")/" "$copie"
    # grub.cfg de PrimTux 9 se termine par un « EOF » oublié, que GRUB lit
    # comme une commande inconnue.
    [ "$menu" = /boot/grub/grub.cfg ] && sed -i '${/^EOF$/d}' "$copie"
    ajouter_installation_auto "$menu" "$copie"
    ajouter_test_memoire "$menu" "$copie"
    if [ "$INSTALLATION" = automatique ]; then
        case "$menu" in
            /boot/grub/grub.cfg)
                # Entrées : 0 Essayer, 1 Installer, 2 Installer automatiquement.
                sed -i 's/^set default=0$/set default=2\nset timeout=20/' "$copie" ;;
            /boot/grub/live-theme/theme.txt)
                sed -i "s/^title-text: \"Occitux\"$/title-text: \"$AVERTISSEMENT\"/" "$copie" ;;
            /isolinux/isolinux.cfg)
                sed -i 's/^timeout 0$/timeout 200/' "$copie" ;;
            /isolinux/menu.cfg)
                sed -i "s/^menu title Occitux$/menu title $(sans_accents "$AVERTISSEMENT")/" "$copie" ;;
            /isolinux/live.cfg)
                sed -i '/^  menu default$/d' "$copie" ;;
            /isolinux/install.cfg)
                sed -i 's/^\(label installauto\)$/\1\n  menu default/' "$copie" ;;
        esac
    fi
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

# 6. Nouvelle ISO : copie de l'originale, fichiers modifiés remplacés.
echo "Écriture de $SORTIE..."
rm -f "$SORTIE"
xorriso -indev "$ISO" -outdev "$SORTIE" \
    -compliance iso_9660_level=3 \
    -volid "Occitux" \
    "${REMPLACER[@]}" \
    -boot_image any replay
(cd "$(dirname "$SORTIE")" && sha256sum "$(basename "$SORTIE")" > "$(basename "$SORTIE").sha256")

echo "Terminé : $SORTIE"
[ "$INSTALLATION" = automatique ] && echo "ISO de déploiement : tout PC démarré dessus s'installe seul et perd son disque."
exit 0
