#!/usr/bin/env python3
"""Proposer des contextes à examiner, jamais valider une traduction."""
import csv
import re
import sys
from corpus import RACINE, lire, normaliser

corpus = list(lire())
debut = int(sys.argv[1]) if len(sys.argv) > 1 else 1
fin = int(sys.argv[2]) if len(sys.argv) > 2 else 999
for i, t in enumerate(csv.DictReader((RACINE / "outils/termes.csv").open(), delimiter=";"), 1):
    if not debut <= i <= fin:
        continue
    motif = re.compile(r"(?<!\w)" + re.escape(normaliser(t["candidat"])) + r"(?!\w)")
    resultats = [r for r in corpus if motif.search(normaliser(r["oc"]))]
    resultats.sort(key=lambda r: (normaliser(t["frances"]) not in normaliser(r["fr"]), len(r["oc"])))
    if resultats:
        r = resultats[0]
        print(f"{i} {t['clau']} : {t['candidat']} [{r['id']}] {r['oc'][:220]} | {r['fr'][:160]}")
    else:
        print(f"{i} {t['clau']} : {t['candidat']} [ABSENT]")
