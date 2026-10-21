#!/usr/bin/env python3
"""Recherche locale dans Lo Congrès websites Corpus v1.0 (CC BY 4.0)."""
import argparse
import hashlib
import json
import re
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
FICHIER = RACINE / "sources/oc-gascon-grclass_fr.csv"
SHA_MD5 = "c431e8f5cb36aa3a89896e3586de0896"


def lire():
    contenu = FICHIER.read_bytes()
    if hashlib.md5(contenu).hexdigest() != SHA_MD5:
        raise ValueError("Le corpus diffère de la version 1.0 référencée sur Zenodo")
    texte = contenu.decode("utf-8")
    motif = re.compile(r"(.*?)§oc-gascon-grclass§(.*?)§fr(?:\r?\n|$)", re.S)
    fin = 0
    ligne = 1
    for i, m in enumerate(motif.finditer(texte), 1):
        if m.start() != fin:
            raise ValueError("Segment du corpus non reconnu")
        fin = m.end()
        yield {"id": f"C{i:05d}", "ligne": ligne,
               "oc": m[1].strip(), "fr": m[2].strip()}
        ligne += m[0].count("\n")
    if texte[fin:].strip():
        raise ValueError("Fin du corpus non reconnue")


def normaliser(texte):
    return texte.casefold().replace("’", "'")


def chercher(requete, champ="oc", mot=False):
    expression = re.escape(normaliser(requete))
    if mot:
        expression = r"(?<!\w)" + expression + r"(?!\w)"
    return [r for r in lire() if re.search(expression, normaliser(r[champ]))]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("requete", nargs="?", default="")
    p.add_argument("--fr", action="store_true", help="rechercher côté français")
    p.add_argument("--mot", action="store_true", help="forme entière, accents conservés")
    p.add_argument("--id", help="afficher une attestation C00001")
    p.add_argument("--limite", type=int, default=8)
    p.add_argument("--json", action="store_true")
    a = p.parse_args()
    lignes = ([r for r in lire() if r["id"] == a.id] if a.id else
              chercher(a.requete, "fr" if a.fr else "oc", a.mot))
    print(f"{len(lignes)} résultat(s)")
    for r in lignes[:a.limite]:
        print(json.dumps(r, ensure_ascii=False) if a.json else
              f"{r['id']} (ligne {r['ligne']}) : {r['oc']}\n  FR : {r['fr']}")


if __name__ == "__main__":
    main()
