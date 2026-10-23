#!/bin/sh
# choisir-disque.sh : désigne le disque effacé par l'installation automatique.
#
# Lancé par l'installateur (partman/early_command) depuis la clé USB. Choisit
# le plus grand disque interne : jamais la clé qui a démarré le PC, jamais un
# disque USB ou amovible, jamais un lecteur optique.
set -e

journal() { echo "occitux : $*" >&2; logger -t occitux "$*" 2>/dev/null || true; }

# Disque qui porte le support d'installation (clé USB : /cdrom est une de ses
# partitions ; ISO montée par Ventoy : on remonte jusqu'au disque).
support=$(findmnt -n -o SOURCE /cdrom 2>/dev/null || true)
support_disque=
if [ -n "$support" ] && [ -b "$support" ]; then
    support_disque=$(lsblk -no PKNAME "$support" 2>/dev/null | head -n1)
    [ -n "$support_disque" ] || support_disque=$(basename "$support")
fi

meilleur=
taille_max=0
lsblk -dn -b -P -o NAME,TYPE,RM,RO,TRAN,SIZE | while read -r ligne; do
    eval "$ligne"
    [ "$TYPE" = disk ] || continue
    [ "$RM" = 0 ] || continue
    [ "$RO" = 0 ] || continue
    [ "$TRAN" != usb ] || continue
    [ "$NAME" != "$support_disque" ] || continue
    case "$NAME" in loop*|zram*|sr*|fd*|ram*|dm-*|md*) continue ;; esac
    echo "$SIZE $NAME"
done | sort -n | tail -n1 | {
    read -r taille_max meilleur || true
    if [ -z "$meilleur" ]; then
        journal "aucun disque interne trouvé : installation impossible"
        exit 1
    fi
    journal "disque choisi : /dev/$meilleur ($((taille_max / 1000000000)) Go)"
    debconf-set partman-auto/disk "/dev/$meilleur"
    debconf-set grub-installer/bootdev "/dev/$meilleur"
}
