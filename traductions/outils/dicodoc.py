#!/usr/bin/env python3
"""Consultation ponctuelle d'une entrée Dicodòc (Per Noste par défaut), sans archivage des définitions.

Dicodòc : tous droits réservés. Ne pas utiliser pour extraire le dictionnaire.
"""
import argparse
import re
from html import unescape
from urllib.parse import urlencode
from urllib.request import urlopen


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("mot", help="une entrée française à consulter")
    p.add_argument("--dic", default="PNST",
                   help="code du dictionnaire Dicodòc (PNST : Per Noste gascon ; "
                        "LAUS : Laux languedocien ; BASIC : Basic gascon/languedocien)")
    a = p.parse_args()
    url = "https://dicodoc.eu/oc/diccionaris?" + urlencode({
        "option": "com_dicodoc", "view": "search", "Itemid": "168",
        "type": "fr-oc", "dic[]": a.dic, "q": a.mot})
    print(url)
    with urlopen(url, timeout=30) as r:
        page = r.read().decode("utf-8")
    resultats = page.split('<div id="dicodoc_results">', 1)
    if len(resultats) != 2:
        raise SystemExit("Résultats non trouvés, vérifier le formulaire sur le site")
    trouve = False
    for ligne in re.findall(r"<tr\b.*?</tr>", resultats[1], re.S):
        colonnes = re.findall(r"<td\b[^>]*>(.*?)</td>", ligne, re.S)
        textes = [unescape(re.sub(r"<[^>]+>", " ", c)).strip() for c in colonnes]
        if textes and textes[0].casefold().split(",")[0].strip() == a.mot.casefold():
            print(" | ".join(re.sub(r"\s+", " ", t) for t in textes))
            trouve = True
    if not trouve:
        print("Pas d'entrée exactement homographe dans les résultats affichés.")


if __name__ == "__main__":
    main()
