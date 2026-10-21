#!/bin/bash
# construire-iso.sh : fabrique l'ISO Occitux à partir de l'ISO officielle PrimTux.
#
#   sudo ./construire/construire-iso.sh <PrimTux.iso> <occitux_x.y.z_all.deb> [sortie.iso]
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

nettoyer() {
    local i
    for ((i = ${#MONTAGES[@]} - 1; i >= 0; i--)); do
        umount -l "${MONTAGES[i]}" 2>/dev/null || true
    done
    rm -rf "$TRAVAIL"
}
trap nettoyer EXIT

# 2. Extraction du système.
echo "Extraction du système (plusieurs minutes)..."
xorriso -osirrox on -indev "$ISO" \
    -extract /casper/filesystem.squashfs "$TRAVAIL/filesystem.squashfs" \
    -extract /md5sum.txt "$TRAVAIL/md5sum.txt" 2>/dev/null \
    || die "pas de /casper/filesystem.squashfs dans l'ISO : est-ce bien une PrimTux basée sur Mint ?"
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

rm -f "$RACINE/tmp/occitux.deb" "$RACINE/usr/sbin/policy-rc.d"
rm -f "$RACINE/etc/resolv.conf"
mv "$TRAVAIL/resolv.conf.origine" "$RACINE/etc/resolv.conf"
# shellcheck disable=SC2016 # format de dpkg-query, pas une variable du shell
chroot "$RACINE" dpkg-query -W --showformat='${Package} ${Version}\n' > "$TRAVAIL/filesystem.manifest"
for ((i = ${#MONTAGES[@]} - 1; i >= 0; i--)); do umount "${MONTAGES[i]}"; done
MONTAGES=()

# 4. Fermeture du système, avec la compression d'origine.
echo "Compression du système ($COMPRESSION, plusieurs minutes)..."
du -sx --block-size=1 "$RACINE" | cut -f1 > "$TRAVAIL/filesystem.size"
mksquashfs "$RACINE" "$TRAVAIL/filesystem.squashfs" -comp "$COMPRESSION" -noappend -quiet

# Le contrôle d'intégrité du menu de démarrage lit md5sum.txt.
for f in filesystem.squashfs filesystem.manifest filesystem.size; do
    somme=$(md5sum "$TRAVAIL/$f" | cut -d' ' -f1)
    sed -i "s|^[0-9a-f]\{32\}  \./casper/$f\$|$somme  ./casper/$f|" "$TRAVAIL/md5sum.txt"
done

# 5. Nouvelle ISO : copie de l'originale, fichiers modifiés remplacés.
echo "Écriture de $SORTIE..."
rm -f "$SORTIE"
xorriso -indev "$ISO" -outdev "$SORTIE" \
    -compliance iso_9660_level=3 \
    -map "$TRAVAIL/filesystem.squashfs" /casper/filesystem.squashfs \
    -map "$TRAVAIL/filesystem.manifest" /casper/filesystem.manifest \
    -map "$TRAVAIL/filesystem.size" /casper/filesystem.size \
    -map "$TRAVAIL/md5sum.txt" /md5sum.txt \
    -boot_image any replay
(cd "$(dirname "$SORTIE")" && sha256sum "$(basename "$SORTIE")" > "$(basename "$SORTIE").sha256")

echo "Terminé : $SORTIE"
