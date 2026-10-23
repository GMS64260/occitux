#!/bin/bash
# depot-apt.sh : construit le dépôt apt d'Occitux (fichiers statiques, servis
# par GitHub Pages) à partir des paquets .deb donnés, et le signe.
#
#   ./construire/depot-apt.sh <dossier-du-depot> <occitux_x.y.z_all.deb>...
#
# Le dossier peut déjà contenir un dépôt (branche gh-pages) : les anciens
# paquets de pool/ sont gardés, les index sont refaits. La clé de signature
# est celle du trousseau GNUPGHOME courant (en CI : secret OCCITUX_CLE_APT).
#
# Sur un PC : deb [signed-by=/usr/share/keyrings/occitux.gpg]
#             https://gms64260.github.io/occitux occitux main
set -euo pipefail

[ $# -ge 2 ] || { echo "usage : $0 <dossier> <paquet.deb>..." >&2; exit 1; }
DEPOT=$(realpath -m "$1"); shift
ICI=$(cd "$(dirname "$0")" && pwd)
for outil in apt-ftparchive gpg; do
    command -v "$outil" >/dev/null || { echo "outil manquant : $outil (apt-utils, gnupg)" >&2; exit 1; }
done

mkdir -p "$DEPOT/pool/main/o/occitux" "$DEPOT/dists/occitux/main/binary-amd64"
for deb in "$@"; do cp -f "$deb" "$DEPOT/pool/main/o/occitux/"; done
cp -f "$ICI/../depot/occitux-apt.asc" "$DEPOT/occitux-apt.asc"
gpg --batch --yes --dearmor -o "$DEPOT/occitux.gpg" "$DEPOT/occitux-apt.asc"
cp -f "$ICI/../paquet/etc/apt/sources.list.d/occitux.sources" "$DEPOT/occitux.sources"

cd "$DEPOT"
# Un seul index (amd64) : le paquet est « Architecture: all ».
apt-ftparchive --arch amd64 packages pool > dists/occitux/main/binary-amd64/Packages
gzip -9 -k -f dists/occitux/main/binary-amd64/Packages
apt-ftparchive \
    -o APT::FTPArchive::Release::Origin=Occitux \
    -o APT::FTPArchive::Release::Label=Occitux \
    -o APT::FTPArchive::Release::Suite=occitux \
    -o APT::FTPArchive::Release::Codename=occitux \
    -o APT::FTPArchive::Release::Architectures=amd64 \
    -o APT::FTPArchive::Release::Components=main \
    -o "APT::FTPArchive::Release::Description=Occitux : PrimTux en occitan pour les Calandretas" \
    release dists/occitux > dists/occitux/Release
gpg --batch --yes --armor --detach-sign -o dists/occitux/Release.gpg dists/occitux/Release
gpg --batch --yes --clearsign -o dists/occitux/InRelease dists/occitux/Release

# Page d'accueil du dépôt.
cat > index.html <<'FIN'
<!doctype html><meta charset="utf-8"><title>Dépôt apt Occitux</title>
<h1>Dépôt apt d'Occitux</h1>
<p>Les PC Occitux reçoivent les mises à jour d'ici tout seuls. Pour un PrimTux 9 :</p>
<pre>sudo curl -fsSL https://gms64260.github.io/occitux/occitux.gpg -o /usr/share/keyrings/occitux.gpg
sudo curl -fsSL https://gms64260.github.io/occitux/occitux.sources -o /etc/apt/sources.list.d/occitux.sources
sudo apt update &amp;&amp; sudo apt install occitux</pre>
<p><a href="https://github.com/GMS64260/occitux">Projet Occitux</a> · <a href="pool/main/o/occitux/">paquets</a></p>
FIN
touch .nojekyll
echo "Dépôt prêt dans $DEPOT :"
grep -E '^(Package|Version|Filename):' dists/occitux/main/binary-amd64/Packages
