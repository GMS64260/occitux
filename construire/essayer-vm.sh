#!/bin/bash
# shellcheck disable=SC2054 # les virgules font partie des options de QEMU
# essayer-vm.sh : démarre une ISO Occitux dans QEMU, avec un disque virtuel
# vierge, pour essayer l'installation automatique et le premier démarrage.
#
#   ./construire/essayer-vm.sh <occitux.iso> [dossier-de-travail]
#   OCCITUX_VM_BIOS=oui   démarrage BIOS (sinon UEFI)
#   OCCITUX_VM_DISQUE=oui démarre sur le disque virtuel (après installation)
#   OCCITUX_VM_VNC=:1     affichage VNC au lieu d'une fenêtre
#
# Le moniteur QEMU écoute sur <dossier>/moniteur.sock ; captures d'écran :
#   echo "screendump /tmp/ecran.ppm" | socat - UNIX-CONNECT:<dossier>/moniteur.sock
set -euo pipefail

[ $# -ge 1 ] || { echo "usage : $0 <occitux.iso> [dossier]" >&2; exit 1; }
ISO=$(realpath "$1")
DOSSIER=$(realpath -m "${2:-construction/vm}")
mkdir -p "$DOSSIER"
DISQUE="$DOSSIER/disque.qcow2"
[ -f "$DISQUE" ] || qemu-img create -q -f qcow2 "$DISQUE" 40G

args=(
    -name Occitux -machine q35,accel=kvm -cpu host -smp 2 -m 3072
    -drive "file=$DISQUE,if=virtio,format=qcow2"
    -device virtio-vga -device qemu-xhci -device usb-tablet
    -netdev user,id=n0 -device virtio-net-pci,netdev=n0
    -monitor "unix:$DOSSIER/moniteur.sock,server,nowait"
    -serial "file:$DOSSIER/serie.log"
    -rtc base=localtime
)
if [ "${OCCITUX_VM_DISQUE:-non}" != oui ]; then
    # La clé USB : l'ISO sur un disque USB, comme sur un vrai PC.
    args+=(-drive "file=$ISO,if=none,id=cle,format=raw,readonly=on"
           -device usb-storage,bus=usb-bus.0,drive=cle,removable=on
           -boot order=c,menu=on)
    # Avec un disque vierge, le firmware passe au support USB.
fi
if [ "${OCCITUX_VM_BIOS:-non}" != oui ]; then
    VARS="$DOSSIER/OVMF_VARS.fd"
    [ -f "$VARS" ] || cp /usr/share/OVMF/OVMF_VARS_4M.fd "$VARS"
    args+=(-drive if=pflash,format=raw,readonly=on,file=/usr/share/OVMF/OVMF_CODE_4M.fd
           -drive "if=pflash,format=raw,file=$VARS")
fi
if [ -n "${OCCITUX_VM_VNC:-}" ]; then
    args+=(-display none -vnc "$OCCITUX_VM_VNC")
fi
exec qemu-system-x86_64 "${args[@]}"
