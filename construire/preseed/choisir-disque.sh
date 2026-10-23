#!/bin/sh
# choisir-disque.sh : désigne le disque effacé par l'installation automatique.
#
# Lancé par l'installateur (partman/early_command, via /bin/preseed_command,
# donc sous l'interface debconf d'Ubiquity) depuis la clé USB. Choisit le plus
# grand disque interne : jamais la clé qui a démarré le PC, jamais un disque
# USB ou amovible, jamais un lecteur optique.
#
# Avec « occitux.trace » sur la ligne de commande du noyau, la trace complète
# va sur le port série (/dev/ttyS0), pour les essais en machine virtuelle.
set -e
if grep -qw occitux.trace /proc/cmdline 2>/dev/null && [ -c /dev/ttyS0 ]; then
    exec 2>>/dev/ttyS0
    set -x
fi

journal() { echo "occitux : $*" >&2; logger -t occitux "$*" 2>/dev/null || true; }

# Réponse debconf. Sous preseed_command, le module de confiance de debconf est
# disponible ; la question peut ne pas exister encore (seul son modèle existe) :
# on l'enregistre alors.
if [ -n "${DEBIAN_HAS_FRONTEND:-}" ]; then
    . /usr/share/debconf/confmodule
    definir() {
        db_set "$1" "$2" 2>/dev/null && return 0
        db_register "$1" "$1" || true
        db_set "$1" "$2"
    }
else
    definir() { debconf-set "$1" "$2"; }
fi

# Disque qui porte le support d'installation (clé USB : /cdrom est une de ses
# partitions ; ISO montée par Ventoy : on remonte jusqu'au disque).
support=$(findmnt -n -o SOURCE /cdrom 2>/dev/null || true)
support_disque=
if [ -n "$support" ] && [ -b "$support" ]; then
    support_disque=$(lsblk -no PKNAME "$support" 2>/dev/null | head -n1 || true)
    [ -n "$support_disque" ] || support_disque=$(basename "$support")
fi
journal "support d'installation : ${support:-?} (disque ${support_disque:-?})"

disques=$(lsblk -dn -b -P -o NAME,TYPE,RM,RO,TRAN,SIZE)
journal "disques : $(echo "$disques" | tr '\n' ' ')"
meilleur=$(echo "$disques" | while read -r ligne; do
    eval "$ligne"
    [ "$TYPE" = disk ] || continue
    [ "$RM" = 0 ] || continue
    [ "$RO" = 0 ] || continue
    [ "$TRAN" != usb ] || continue
    [ "$NAME" != "$support_disque" ] || continue
    case "$NAME" in loop*|zram*|sr*|fd*|ram*|dm-*|md*) continue ;; esac
    echo "$SIZE $NAME"
done | sort -n | tail -n1)
taille=${meilleur%% *}
meilleur=${meilleur#* }

if [ -z "$meilleur" ]; then
    journal "aucun disque interne trouvé : installation impossible"
    exit 1
fi
journal "disque choisi : /dev/$meilleur ($((taille / 1000000000)) Go)"
definir partman-auto/disk "/dev/$meilleur"
definir grub-installer/bootdev "/dev/$meilleur"
