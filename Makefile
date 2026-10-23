VERSION := $(shell sed -n 's/^Version: //p' paquet/DEBIAN/control)
DEB     := construction/occitux_$(VERSION)_all.deb
SCRIPTS := paquet/usr/sbin/occitux-config paquet/DEBIAN/postinst paquet/DEBIAN/prerm paquet/DEBIAN/postrm \
           construire/construire-iso.sh construire/essayer-vm.sh construire/depot-apt.sh \
           construire/preseed/choisir-disque.sh construire/preseed/apres-installation.sh

# Catalogues béarnais : traductions/gascon/<domaine>.po → <domaine>.mo, installés
# dans /usr/share/occitux/locale/oc@gascon. dpkg écarterait tout fichier posé
# directement dans /usr/share/locale (localepurge de PrimTux) : occitux-config
# y crée un lien oc@gascon vers ce dossier (voir LANGUE=bearnes).
PO      := $(wildcard traductions/gascon/*.po)
# Tables de textes (menu des élèves, écran de connexion, menus de démarrage…)
# et logo : /usr/share/occitux/textes et /usr/share/occitux/identite.
CSV     := $(wildcard traductions/*.csv)
IDENTITE := identite/occitux.svg identite/occitux.png identite/occitux-blanc.png
RACINE  := construction/racine
CATALOGUES := $(RACINE)/usr/share/occitux/locale/oc@gascon/LC_MESSAGES

.PHONY: paquet iso verifier propre

paquet: $(DEB)

$(DEB): $(shell find paquet -type f) $(PO) $(CSV) $(IDENTITE) depot/occitux-apt.asc
	rm -rf $(RACINE)
	mkdir -p $(RACINE)
	cp -a paquet/. $(RACINE)/
	chmod 0755 $(RACINE)/usr/sbin/occitux-config $(RACINE)/usr/share/occitux/traduire.py \
	           $(RACINE)/DEBIAN/postinst $(RACINE)/DEBIAN/prerm $(RACINE)/DEBIAN/postrm
	mkdir -p $(RACINE)/usr/share/occitux/textes $(RACINE)/usr/share/occitux/identite
	cp $(CSV) $(RACINE)/usr/share/occitux/textes/
	cp $(IDENTITE) $(RACINE)/usr/share/occitux/identite/
	gpg --batch --yes --dearmor -o $(RACINE)/usr/share/keyrings/occitux.gpg depot/occitux-apt.asc
	mkdir -p $(CATALOGUES)
	for po in $(PO); do \
		msgfmt --check -o $(CATALOGUES)/$$(basename $$po .po).mo $$po || exit 1; \
	done
	dpkg-deb --root-owner-group -Zxz --build $(RACINE) $@

# make iso ISO=/chemin/PrimTux9-M22.3-64bit-2026-02-27.iso
iso: $(DEB)
	@test -n "$(ISO)" || { echo "usage : make iso ISO=/chemin/vers/PrimTux.iso"; exit 1; }
	sudo ./construire/construire-iso.sh "$(ISO)" $(DEB) construction/occitux-$(VERSION).iso

verifier:
	shellcheck $(SCRIPTS)
	python3 -m py_compile paquet/usr/share/occitux/traduire.py
	bash -n construire/construire-iso.sh

propre:
	rm -rf construction
