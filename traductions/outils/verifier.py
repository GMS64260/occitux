#!/usr/bin/env python3
"""Vérifier les deltas et leur repli avec le programme GNU gettext réel."""
import csv
import json
import os
import re
import subprocess
from collections import Counter
from pathlib import Path
import polib
from corpus import RACINE as R, lire, normaliser
from glossaire import catalogues, lire_glossaire
from catalogues import formats, accelerateurs, manuelles, remplacer_mot, adapter, regles
from inventorier import DOMAINES


def mots(texte):
    return set(re.findall(r"[^\W\d_]+", normaliser(texte.replace("_", ""))))


def main():
    assert remplacer_mot("O_metre", "metre", "méter") == "O_metre"
    assert remplacer_mot("_Dobrir", "dobrir", "obrir") == "_Obrir"
    assert remplacer_mot("A_pondre", "apondre", "ajustar") == "_Ajustar"
    corpus = list(lire())
    assert len(corpus) == 8552
    ids = {c["id"] for c in corpus}
    glossaire = lire_glossaire()
    gloss = {g["clau"]: g for g in glossaire}
    assert len(gloss) == len(glossaire)
    assert all(g["source_forme"] for g in glossaire if g["estat"] == "atteste")
    attestes = set().union(*(mots(c["oc"]) for c in corpus))
    attestes |= set().union(*(mots(g["bearnes"]) for g in glossaire if g["estat"] == "atteste"))
    oc, fr = catalogues(), catalogues("fr")
    reg = regles(glossaire)
    # Toute traduction explicite doit correspondre à une vraie entrée source.
    for m in manuelles():
        assert oc[m["domaine"]].find(m["msgid"]) is not None, ("Clé manuelle inconnue", m)
        for terme in m["termes"]:
            assert terme in gloss, terme
        for source in m["sources"]:
            if source.startswith("G:"):
                assert gloss[source[2:]]["estat"] == "atteste", source
            elif source.startswith("https://dicodoc.eu/oc/diccionaris?"):
                assert "dic%5B%5D=PNST" in source and "&q=" in source, source
            else:
                assert source in ids, source
        e_fr = fr[m["domaine"]].find(m["msgid"])
        adapte = adapter(m["bearnes"], m["msgid"], e_fr.msgstr if e_fr else "", reg)[0]
        assert adapte == m["bearnes"], ("Incohérence avec le glossaire", m, adapte)
    racine = R / "construction/locale"
    quantites = Counter()
    problemes = []
    for d in DOMAINES:
        p = R / "gascon" / f"{d}.po"
        delta = polib.pofile(str(p))
        assert delta.metadata["Language"] == "oc"
        assert "charset=UTF-8" in delta.metadata["Content-Type"]
        cles = set()
        for e in delta:
            cle = (e.msgctxt, e.msgid)
            assert cle not in cles, (d, cle)
            cles.add(cle)
            ancien = oc[d].find(e.msgid, msgctxt=e.msgctxt)
            assert ancien is not None, (d, cle)
            assert not e.fuzzy and not e.obsolete
            assert e.msgid_plural == ancien.msgid_plural
            assert e.msgstr and e.msgstr != ancien.msgstr, ("Entrée sans différence", d, cle)
            assert formats(e.msgstr) == formats(e.msgid), ("Paramètres", d, cle)
            assert accelerateurs(e.msgstr) == accelerateurs(e.msgid), ("Raccourcis", d, cle)
            assert re.findall(r"<[^>]+>", e.msgstr) == re.findall(r"<[^>]+>", ancien.msgstr), ("Balises", d, cle)
            assert "—" not in e.msgstr, (d, cle)
            for mot in mots(e.msgstr) - mots(ancien.msgstr) - mots(e.msgid) - attestes:
                problemes.append((d, e.msgid, mot))
        sortie = racine / "oc@gascon/LC_MESSAGES" / f"{d}.mo"
        sortie.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["msgfmt", "--check", "-o", "/dev/null", str(p)], check=True)
        subprocess.run(["msgfmt", "--check", "-o", str(sortie), str(p)], check=True)
        for langue, original in [("oc", oc[d]), ("fr", fr[d])]:
            destination = racine / langue / "LC_MESSAGES" / f"{d}.mo"
            destination.parent.mkdir(parents=True, exist_ok=True)
            original.save_as_mofile(str(destination))
        env = dict(os.environ, LC_ALL="fr_FR.UTF-8", LANGUAGE="oc_FR@gascon:oc:fr", TEXTDOMAINDIR=str(racine))
        essais = []
        entree_delta = next((e for e in delta if not e.msgctxt and not e.msgid_plural), None)
        entree_oc = next((e for e in oc[d] if not e.msgctxt and not e.msgid_plural and (e.msgctxt, e.msgid) not in cles and e.msgstr != e.msgid), None)
        entree_fr = next((e for e in fr[d] if not e.msgctxt and not e.msgid_plural and not oc[d].find(e.msgid) and e.msgstr != e.msgid), None)
        for niveau, e in [("béarnais", entree_delta), ("occitan", entree_oc), ("français", entree_fr)]:
            if e is None:
                continue
            resultat = subprocess.check_output(["gettext", "-d", d, "--", e.msgid], env=env).decode("utf-8")
            assert resultat == e.msgstr, ("Repli GNU gettext", d, niveau, e.msgid, resultat, e.msgstr)
            quantites[niveau] += 1
        print(f"{d} : {len(delta)} chaînes, msgfmt et repli vérifiés")
    assert not problemes, ("Formes nouvelles sans attestation lexicale", problemes)
    assert all(quantites[n] for n in ["béarnais", "occitan", "français"]), quantites
    with (R / "occitux.csv").open(newline="") as f:
        textes = list(csv.DictReader(f, delimiter=";"))
    assert set(textes[0]) == {"clau", "frances", "bearnes"}
    sources = list(csv.DictReader((R / "occitux-sources.csv").open(), delimiter=";"))
    assert {r["clau"] for r in sources} == {r["clau"] for r in textes}
    variables = re.compile(r"\$(?:\{)?([A-Za-z_][A-Za-z_0-9]*)")
    for t in textes:
        assert Counter(variables.findall(t["frances"])) == Counter(variables.findall(t["bearnes"])), t
        assert formats(t["frances"]) == formats(t["bearnes"]) or t["clau"] == "config.gcompris", t
        assert "—" not in t["bearnes"]
        assert not (mots(t["bearnes"]) - mots(t["frances"]) - attestes), t
    for ligne in sources:
        for source in ligne["sources"].split(" + "):
            if source.startswith("glossari:"):
                assert gloss[source.removeprefix("glossari:")]["estat"] == "atteste", source
            else:
                assert source in ids, source
    rapport = {"notions": len(glossaire), "notions_conservees": sum(g["estat"] == "conserve" for g in glossaire),
               "textes_occitux": len(textes), "essais_gettext": dict(quantites),
               "note": "Validation technique et traçabilité des formes nouvelles ; ne certifie pas les traductions amont conservées."}
    (R / "construction/verification.json").write_text(json.dumps(rapport, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(rapport, ensure_ascii=False))


if __name__ == "__main__":
    main()
