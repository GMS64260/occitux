VERSION := $(shell sed -n 's/^Version: //p' paquet/DEBIAN/control)
DEB     := construction/occitux_$(VERSION)_all.deb
SCRIPTS := paquet/usr/sbin/occitux-config paquet/DEBIAN/postinst paquet/DEBIAN/postrm construire/construire-iso.sh

# Catalogues béarnais : traductions/gascon/<domaine>.po → <domaine>.mo, installés
# dans /usr/share/locale/oc@gascon (voir LANGUE=bearnes).
PO      := $(wildcard traductions/gascon/*.po)
RACINE  := construction/racine

.PHONY: paquet iso verifier propre

paquet: $(DEB)

$(DEB): $(shell find paquet -type f) $(PO)
	rm -rf $(RACINE)
	mkdir -p $(RACINE)
	cp -a paquet/. $(RACINE)/
	chmod 0755 $(RACINE)/usr/sbin/occitux-config $(RACINE)/DEBIAN/postinst $(RACINE)/DEBIAN/postrm
	mkdir -p $(RACINE)/usr/share/locale/oc@gascon/LC_MESSAGES
	for po in $(PO); do \
		msgfmt --check -o $(RACINE)/usr/share/locale/oc@gascon/LC_MESSAGES/$$(basename $$po .po).mo $$po || exit 1; \
	done
	dpkg-deb --root-owner-group -Zxz --build $(RACINE) $@

# make iso ISO=/chemin/PrimTux9-M22.3-64bit-2026-02-27.iso
iso: $(DEB)
	@test -n "$(ISO)" || { echo "usage : make iso ISO=/chemin/vers/PrimTux.iso"; exit 1; }
	sudo ./construire/construire-iso.sh "$(ISO)" $(DEB) construction/occitux-$(VERSION).iso

verifier:
	shellcheck $(SCRIPTS)

propre:
	rm -rf construction
