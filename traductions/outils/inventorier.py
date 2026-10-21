#!/usr/bin/env python3
"""Inventorier les paquets téléchargés et décompiler leurs catalogues."""
import hashlib
import json
import subprocess
from pathlib import Path

R = Path(__file__).resolve().parents[1]
DOMAINES = ("xfce4-panel", "xfce4-session", "xfdesktop", "thunar", "xfwm4",
            "tuxpaint", "lightdm", "ristretto", "xfce4-pulseaudio-plugin",
            "lightdm-gtk-greeter")


def main():
    paquets = []
    for deb in sorted((R / "sources").glob("*.deb")):
        champs = subprocess.check_output(
            ["dpkg-deb", "-f", str(deb), "Package", "Version", "Architecture"], text=True)
        info = dict(ligne.split(": ", 1) for ligne in champs.strip().splitlines())
        info["fichier"] = deb.name
        info["sha256"] = hashlib.sha256(deb.read_bytes()).hexdigest()
        info["catalogues"] = []
        racine = R / "sources/extraits" / info["Package"]
        racine.mkdir(parents=True, exist_ok=True)
        subprocess.run(["dpkg-deb", "-x", str(deb), str(racine)], check=True)
        for langue in ("oc", "fr"):
            for mo in sorted(racine.rglob("*.mo")):
                if mo.parent.parent.name != langue or mo.stem not in DOMAINES:
                    continue
                po = R / "sources/po" / langue / (mo.stem + ".po")
                po.parent.mkdir(parents=True, exist_ok=True)
                subprocess.run(["msgunfmt", str(mo), "-o", str(po)], check=True)
                # Un MO vide (LightDM oc dans Noble) ne produit aucun fichier.
                info["catalogues"].append({"langue": langue, "domaine": mo.stem,
                    "chemin": str(mo.relative_to(racine)),
                    "sha256": hashlib.sha256(mo.read_bytes()).hexdigest(),
                    "vide": not po.exists()})
        paquets.append(info)
    (R / "provenance.json").write_text(json.dumps({
        "distribution": "Ubuntu 24.04 noble / noble-updates",
        "date_consultation": "2026-10-21",
        "corpus": {"titre": "Lo Congrès websites Corpus v1.0",
                   "auteur": "Aure Séguier ; Lo Congrès",
                   "url": "https://zenodo.org/records/12192029",
                   "licence": "CC BY 4.0",
                   "fichier": "oc-gascon-grclass_fr.csv",
                   "md5": "c431e8f5cb36aa3a89896e3586de0896", "entrees": 8552},
        "paquets": paquets}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
