#!/usr/bin/env python3
"""Documenter les recherches infructueuses et les phrases conservées."""
import csv
import json
from collections import Counter
from corpus import RACINE as R, lire, normaliser
from glossaire import lire_glossaire, limite_mot
from catalogues import FLEXIONS_DIFFEREES, md


def main():
    corpus = list(lire())
    glossaire = lire_glossaire()
    candidats = {r["clau"]: r for r in csv.DictReader((R / "outils/termes.csv").open(), delimiter=";")}
    lignes = ["# Formes conservées et limites de validation", "",
        "Une forme non attestée dans le sens demandé ne devient pas béarnaise par ressemblance.",
        "Les formes ci-dessous restent celles des catalogues occitans. Les cases vides signalent",
        "une absence dans les paquets examinés. Aucune entrée n'est ajoutée pour combler cette absence.", "",
        "## Notions du glossaire", "",
        "| Notion | Forme conservée | Recherche et résultat |", "|---|---|---|"]
    for r in glossaire:
        if r["estat"] != "conserve":
            continue
        t = candidats[r["clau"]]
        noc = sum(bool(limite_mot(t["candidat"]).search(normaliser(c["oc"]))) for c in corpus)
        nfr = sum(normaliser(t["frances"]) in normaliser(c["fr"]) for c in corpus)
        recherche = f"Corpus : {t['candidat']} (forme entière, {noc} occurrences), {t['frances']} (côté français, {nfr} occurrences). " + r["notes"]
        lignes.append("| " + " | ".join(md(x) for x in [r["frances"], r["languedocien"] or "Absente", recherche]) + " |")
    lignes += ["", "## Flexions non introduites", "",
        "Une attestation du singulier ne constitue pas ici une attestation littérale du pluriel.",
        "Les formes suivantes n'ont aucune occurrence exacte dans le corpus. Elles ne sont pas",
        "fabriquées automatiquement dans les PO ; les chaînes concernées restent en occitan.", "",
        "| Source oc | Forme cherchée | Recherche |", "|---|---|---|"]
    for oc, be in FLEXIONS_DIFFEREES.items():
        n = sum(bool(limite_mot(be).search(normaliser(c["oc"]))) for c in corpus)
        lignes.append(f"| {oc} | {be} | Mot entier côté occitan : {n} résultat. Singulier vérifié dans le glossaire. |")
    audit = list(csv.DictReader((R / "audit.csv").open(), delimiter=";"))
    differes = [r for r in audit if r["statut"] == "differe"]
    compte = Counter(r["domaine"] for r in differes)
    lignes += ["", "## Chaînes conservées", "",
        f"{len(differes)} chaînes ont des différences repérées mais ne sont pas livrées dans le delta.",
        "Elles figurent individuellement dans [audit.md](audit.md) et [audit.csv](audit.csv),",
        "avec leur clé exacte et leur motif : conjugaison, construction de phrase, pluriels gettext,",
        "sens technique non établi, ou défaut des paramètres et raccourcis dans la source.",
        "Le glossaire ne valide pas à lui seul la syntaxe de toutes les phrases qui emploient ses mots.", "",
        "| Domaine | Chaînes conservées |", "|---|---:|"]
    lignes += [f"| {d} | {n} |" for d, n in compte.items()]
    lignes += ["", "## Variantes et sens à ne pas confondre", "",
        "- `nòu` peut désigner neuf ou nouveau. Le mot de l'horloge n'est pas remplacé par `navèth`.",
        "- `ret` est féminin dans les catalogues sources ; `hialat` est masculin. Un remplacement sans accord est écarté.",
        "- `sens` peut être un nom ou signifier sans. `font` peut être source ou apparaître dans un contexte typographique.",
        "- `son` peut être un nom, un possessif ou un verbe. L'entrée Per Noste son (audition) sert pour le son de l'ordinateur.",
        "- Le corpus contient des citations languedociennes, notamment des passages narratifs en C038xx et des interfaces en C072xx. L'étiquette du fichier ne les rend pas béarnaises.",
        "- Pour fenêtre, Per Noste distingue notamment `frinèsta`, des formes pyrénéennes `hrièsta` / `herièsta`, et des formes bigourdanes `hièstra` / `hiestra`. La forme commune retenue est aussi attestée dans une interface vidéo en C06017. Aucune de ces indications ne démontre une exclusivité ossaloise.",
        "", "## Reproduire une recherche", "", "```sh",
        "python3 traductions/outils/corpus.py frinèstas --mot",
        "python3 traductions/outils/corpus.py fenêtre --fr",
        "python3 traductions/outils/dicodoc.py fenêtre", "```", "",
        "Le périmètre de livraison est un delta vérifié et conservateur, pas la certification intégrale",
        "des traductions amont. Les chaînes différées restent un travail à terminer, explicitement visible.", ""]
    (R / "incertituds.md").write_text("\n".join(lignes), encoding="utf-8")


if __name__ == "__main__":
    main()
