#!/usr/bin/env python3
"""Assembler le glossaire à partir des choix relus, du corpus et des MO Ubuntu."""
import csv
import json
import re
from urllib.parse import urlencode
import polib
from corpus import RACINE as R, lire, normaliser
from inventorier import DOMAINES


def limite_mot(mot):
    return re.compile(r"(?<!\w)" + re.escape(normaliser(mot)) + r"(?!\w)")


def url_dic(mot):
    return "https://dicodoc.eu/oc/diccionaris?" + urlencode({
        "option": "com_dicodoc", "view": "search", "Itemid": "168",
        "type": "fr-oc", "dic[]": "PNST", "q": mot})


def catalogues(langue="oc"):
    return {d: polib.pofile(str(p)) if (p := R / "sources/po" / langue / f"{d}.po").exists()
            else polib.POFile() for d in DOMAINES}


def lire_glossaire():
    with (R / "glossari.csv").open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader((l for l in f if not l.startswith("#")), delimiter=";"))


def extrait(texte, mot):
    m = limite_mot(mot).search(normaliser(texte))
    pos = m.start() if m else 0
    a, b = max(0, pos - 45), min(len(texte), pos + 160)
    return ("…" if a else "") + texte[a:b].replace("\n", " ").replace("—", "-") + ("…" if b < len(texte) else "")


def main():
    corpus = list(lire())
    index = {r["id"]: r for r in corpus}
    decisions = json.loads((R / "outils/decisions.json").read_text())
    cat = catalogues()
    entrees = [(d, e) for d, p in cat.items() for e in p]
    autres = []
    for mo in sorted((R / "sources/extraits/language-pack-oc-base").rglob("*.mo")):
        autres.extend(("language-pack-oc-base/" + mo.stem, e) for e in polib.mofile(str(mo)))
    lignes = []
    for t in csv.DictReader((R / "outils/termes.csv").open(), delimiter=";"):
        cle = t["clau"]
        # Les valeurs de cette colonne sont extraites, jamais retraduites.
        observes, provenances = [], []
        for forme in t["formes_oc"].split("|"):
            motif = limite_mot(forme)
            for d, e in entrees:
                chaines = [e.msgstr] + list(e.msgstr_plural.values())
                for chaine in chaines:
                    sans_raccourci = chaine.replace("_", "")
                    m = motif.search(normaliser(sans_raccourci))
                    if m and normaliser(m[0]) not in [normaliser(v) for v in observes]:
                        observes.append(sans_raccourci[m.start():m.end()])
                        provenances.append(f"{d} : {e.msgid}")
        # Compléter uniquement les notions absentes des neuf applications :
        # les formes proviennent toujours d'un MO Ubuntu, jamais de l'intuition.
        if not observes:
            variantes = t["formes_oc"].split("|")
            motif = re.compile(r"(?<!\w)(?:" + "|".join(re.escape(v) for v in variantes) + r")s?(?!\w)")
            for d, e in entrees + autres:
                for chaine in [e.msgstr] + list(e.msgstr_plural.values()):
                    sans_raccourci = chaine.replace("_", "")
                    m = motif.search(normaliser(sans_raccourci))
                    if m:
                        observes.append(sans_raccourci[m.start():m.end()])
                        provenances.append(f"{d} : {e.msgid}")
                        break
                if observes:
                    break
        forme = decisions["formes"].get(cle, t["candidat"])
        correspondances = [r for r in corpus if limite_mot(forme).search(normaliser(r["oc"]))]
        correspondances.sort(key=lambda r: (normaliser(t["frances"]) not in normaliser(r["fr"]), len(r["oc"])))
        # Les premiers contextes ont été examinés avec examiner.py ; les choix
        # trompeurs (homonymie, citation languedocienne) sont surchargés ci-dessous.
        source, oc, fr, note = "", "", "", ""
        statut = "atteste"
        if cle in decisions["conserver"]:
            statut = "conserve"
            forme = observes[0] if observes else ""
            note = decisions["conserver"][cle]
        elif cle in decisions["dicodoc"]:
            choix = decisions["dicodoc"][cle]
            forme = choix["forme"]
            source = url_dic(choix["mot"])
            oc, fr = forme, choix["mot"]
            note = "Per Noste (gascon), entrée consultée individuellement le 2026-10-21. Forme lexicale choisie, définition non reproduite."
        elif cle in decisions["composes"]:
            choix = decisions["composes"][cle]
            forme = choix["forme"]
            source = " + ".join(choix["sources"]) + " + " + url_dic("démarrer")
            oc = " / ".join(extrait(index[x]["oc"], "aviar") for x in choix["sources"])
            fr = " / ".join(index[x]["fr"] for x in choix["sources"])
            note = choix["note"]
        elif correspondances or cle in decisions["corpus"]:
            r = index[decisions["corpus"][cle]] if cle in decisions["corpus"] else correspondances[0]
            assert limite_mot(forme).search(normaliser(r["oc"])), (cle, r)
            source = r["id"]
            oc, fr = extrait(r["oc"], forme), r["fr"].replace("\n", " ").replace("—", "-")
            note = "Lo Congrès, corpus gascon, CC BY 4.0."
        else:
            statut = "conserve"
            forme = observes[0] if observes else ""
            note = f"Corpus : recherche de {t['candidat']} et de {t['frances']} côté français. Aucune attestation exacte retenue."
        if not observes:
            note += " Forme source absente des catalogues examinés ; colonne languedocienne laissée vide."
        lignes.append(dict(clau=cle, frances=t["frances"], languedocien=" | ".join(observes),
            bearnes=forme, estat=statut, source_forme=source, attestation_oc=oc, attestation_fr=fr,
            source_languedocien=" | ".join(provenances), ossau="", source_ossau="", notes=note))
    with (R / "glossari.csv").open("w", encoding="utf-8", newline="") as f:
        f.write("# Adresse : forme impersonnelle et actions à l'infinitif, pour une interface stable de 3 à 11 ans, sans alternance tu/vous.\n")
        f.write("# Une notion = un choix lexical. Les valeurs conserve restent celles du catalogue oc ; elles ne sont pas certifiées béarnaises.\n")
        f.write("# Cxxxxx : Lo Congrès / Aure Séguier, Lo Congrès websites Corpus v1.0, https://doi.org/10.5281/zenodo.12192029, CC BY 4.0.\n")
        f.write("# Ossau : aucun particularisme attribué sans attestation locale ; pyrénéen ne signifie pas exclusivement ossalois.\n")
        w = csv.DictWriter(f, fieldnames=list(lignes[0]), delimiter=";", lineterminator="\n")
        w.writeheader()
        w.writerows(lignes)
    print(f"{len(lignes)} notions ; {sum(t['estat'] == 'atteste' for t in lignes)} attestées ; "
          f"{sum(t['estat'] == 'conserve' for t in lignes)} conservées.")


if __name__ == "__main__":
    main()
