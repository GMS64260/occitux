VERSION := $(shell sed -n 's/^Version: //p' paquet/DEBIAN/control)
DEB     := construction/occitux_$(VERSION)_all.deb
SCRIPTS := paquet/usr/sbin/occitux-config paquet/DEBIAN/postinst paquet/DEBIAN/postrm construire/construire-iso.sh

.PHONY: paquet iso verifier propre

paquet: $(DEB)

$(DEB): $(shell find paquet -type f)
	mkdir -p construction
	chmod 0755 $(SCRIPTS)
	dpkg-deb --root-owner-group -Zxz --build paquet $@

# make iso ISO=/chemin/PrimTux9-M22.3-64bit-2026-02-27.iso
iso: $(DEB)
	@test -n "$(ISO)" || { echo "usage : make iso ISO=/chemin/vers/PrimTux.iso"; exit 1; }
	sudo ./construire/construire-iso.sh "$(ISO)" $(DEB) construction/occitux-$(VERSION).iso

verifier:
	shellcheck $(SCRIPTS)

propre:
	rm -rf construction
