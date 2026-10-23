#!/bin/sh
# apres-installation.sh : dernières retouches sur le système installé (/target),
# lancées par l'installateur juste avant l'extinction (ubiquity/success_command).
set -e
cible=/target

journal() { echo "occitux : $*" >&2; logger -t occitux "$*" 2>/dev/null || true; }

# Nom du PC : occitux-xxxx, avec quatre caractères tirés au sort, pour que les
# PC d'une même école se distinguent sur le réseau sans intervention.
suffixe=$(tr -dc a-z0-9 < /dev/urandom | head -c 4 || true)
nom="occitux-${suffixe:-0000}"
echo "$nom" > "$cible/etc/hostname"
sed -i "s/^127\.0\.1\.1\s.*/127.0.1.1\t$nom/" "$cible/etc/hosts"
grep -q '^127\.0\.1\.1' "$cible/etc/hosts" || printf '127.0.1.1\t%s\n' "$nom" >> "$cible/etc/hosts"
journal "nom du PC : $nom"

# Le service de premier démarrage d'Occitux réapplique langue et clavier.
rm -f "$cible/var/lib/occitux/premier-demarrage-fait"
