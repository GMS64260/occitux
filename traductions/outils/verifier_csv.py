#!/usr/bin/env python3
"""Contrôle de forme des tables de substitution : primtuxmenu.csv, systeme.csv, occitux.csv.

Vérifie l'encodage UTF-8, l'en-tête, le nombre de colonnes, l'absence de doublon
de clé ou de chaîne source, les cases vides, et la conservation dans chaque colonne
traduite des éléments techniques de la source : variables {…} et {{ … }}, expansions
shell $VAR et ${…} (pour ${var/motif/texte}, seul le texte de remplacement peut
changer), entités &nbsp;, balises HTML et noms propres non traduisibles.
Il ne juge pas la langue : une table bien formée n'est pas une table validée.
"""
import csv
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
TABLES = {
    "primtuxmenu.csv": ("frances", "occitan", "bearnes"),
    "systeme.csv": ("clau", "frances", "occitan", "bearnes"),
    "occitux.csv": ("clau", "frances", "occitan", "bearnes"),
}
MOTIFS = [
    re.compile(r"\{\{.*?\}\}"),          # {{ jinja }}
    re.compile(r"(?<!\$)\{[^{}\s][^{}]*\}"),  # {variable} ou {e.code}, hors ${…}
    re.compile(r"\$\{[^}/]*(?:/[^}/]*/)?"),  # ${expansion} : nom et motif d'une substitution ${var/motif/…}
    re.compile(r"\$[A-Za-z_][A-Za-z0-9_]*"),  # $VAR
    re.compile(r"&[a-z]+;"),             # &nbsp;
    re.compile(r"<[^>]+>"),              # balises
]
INVARIANTS = ["Occitux", "Jerry", "Koda", "Léon", "Poe", "GCompris", "Firefox", "LibreOffice",
              "VLC", "Qwant", "QwantJunior", "Dns4eu", "USB", "sudo", "PC", "CP", "CE1", "CE2",
              "CM1", "CM2", "6e", "DNS", "Linux"]


def elements(texte):
    trouves = []
    for motif in MOTIFS:
        trouves.extend(motif.findall(texte))
    return sorted(trouves)


def verifier(nom, colonnes):
    chemin = RACINE / nom
    erreurs = []
    brut = chemin.read_bytes()
    try:
        texte = brut.decode("utf-8")
    except UnicodeDecodeError as e:
        return [f"{nom} : UTF-8 invalide ({e})"]
    if texte.startswith("﻿"):
        erreurs.append(f"{nom} : BOM inattendu")
    lignes = list(csv.reader(texte.splitlines(), delimiter=";"))
    if not lignes or tuple(lignes[0]) != colonnes:
        return [f"{nom} : en-tête attendu {';'.join(colonnes)}, trouvé {';'.join(lignes[0]) if lignes else 'rien'}"]
    vus = set()
    sources = set()
    for num, ligne in enumerate(lignes[1:], 2):
        if len(ligne) != len(colonnes):
            erreurs.append(f"{nom}:{num} : {len(ligne)} colonnes au lieu de {len(colonnes)}")
            continue
        enreg = dict(zip(colonnes, ligne))
        identifiant = enreg.get("clau", enreg["frances"])
        if identifiant in vus:
            erreurs.append(f"{nom}:{num} : doublon de {'clé' if 'clau' in enreg else 'chaîne'} {identifiant!r}")
        vus.add(identifiant)
        if "clau" in enreg:
            if not re.fullmatch(r"[a-z]+(\.[a-z_]+)+", enreg["clau"]):
                erreurs.append(f"{nom}:{num} : clé mal formée {enreg['clau']!r}")
            if enreg["frances"] in sources:
                erreurs.append(f"{nom}:{num} : chaîne française déjà présente {enreg['frances']!r}")
            sources.add(enreg["frances"])
        for c in colonnes:
            if enreg[c].strip() == "":
                erreurs.append(f"{nom}:{num} : colonne {c} vide")
        attendus = elements(enreg["frances"])
        for c in ("occitan", "bearnes"):
            if elements(enreg[c]) != attendus:
                erreurs.append(f"{nom}:{num} ({c}) : éléments techniques {attendus} ≠ {elements(enreg[c])}")
            for inv in INVARIANTS:
                motif = re.compile(r"(?<!\w)" + re.escape(inv) + r"(?!\w)")
                if motif.search(enreg["frances"]) and not motif.search(enreg[c]):
                    erreurs.append(f"{nom}:{num} ({c}) : {inv!r} absent de la traduction")
            if re.search(r"(?<!\w)Prim[Tt]ux(?!\w)", enreg[c]) and "PrimTux en occitan" not in enreg[c] and "Entà PrimTux" not in enreg[c] and "Per PrimTux" not in enreg[c]:
                erreurs.append(f"{nom}:{num} ({c}) : PrimTux devrait devenir Occitux")
            if enreg["frances"].endswith(" ") != enreg[c].endswith(" "):
                erreurs.append(f"{nom}:{num} ({c}) : espace final non conservé")
    return erreurs


def main():
    toutes = []
    for nom, colonnes in TABLES.items():
        if not (RACINE / nom).exists():
            toutes.append(f"{nom} : fichier absent")
            continue
        e = verifier(nom, colonnes)
        print(f"{nom} : {'OK' if not e else str(len(e)) + ' erreur(s)'}")
        toutes.extend(e)
    for e in toutes:
        print("  -", e)
    sys.exit(1 if toutes else 0)


if __name__ == "__main__":
    main()
