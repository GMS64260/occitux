#!/usr/bin/python3
"""traduire.py : remplace des textes français par leur traduction dans un fichier.

Les tables sont les CSV de /usr/share/occitux/textes (séparateur « ; ») :
une colonne « frances » (texte exact d'origine) et une colonne par langue
(« occitan », « bearnes »). Les textes sont remplacés entiers, du plus long
au plus court, et seulement s'ils ne sont pas collés à d'autres lettres.
« PrimTux » devient toujours « Occitux », même en français.

    traduire.py --langue oc --textes DIR SOURCE DESTINATION
    traduire.py --langue oc --textes DIR --diapo welcome SOURCE DESTINATION
    traduire.py --langue oc --textes DIR --sqlite BASE [--inverse]
    traduire.py --langue oc --textes DIR --cle lanceur.menu
"""
import argparse
import csv
import glob
import os
import re
import shutil
import sqlite3
import sys

COLONNE = {"oc": "occitan", "bearnes": "bearnes", "fr": "frances"}
MARQUE = re.compile(r"(?<![\w-])Prim[Tt]ux(?![\w-])")


def lire_tables(dossier, colonne, inverse=False):
    """Dictionnaire texte français → traduction, et clés → traduction.

    inverse : toute traduction connue (quelle que soit la langue) → français."""
    textes, cles = {}, {}
    for chemin in sorted(glob.glob(os.path.join(dossier, "*.csv"))):
        with open(chemin, encoding="utf-8", newline="") as f:
            lignes = [l for l in csv.reader(f, delimiter=";") if l and not l[0].startswith("#")]
        if not lignes:
            continue
        entete = [c.strip() for c in lignes[0]]
        if "frances" not in entete:
            continue
        i_fr = entete.index("frances")
        i_cle = entete.index("clau") if "clau" in entete else None
        if inverse:
            colonnes = [i for i, c in enumerate(entete) if c in COLONNE.values() and c != "frances"]
        elif colonne in entete:
            colonnes = [entete.index(colonne)]
        else:
            continue
        for ligne in lignes[1:]:
            if len(ligne) <= max([i_fr] + colonnes):
                continue
            fr = ligne[i_fr]
            for i_tr in colonnes:
                tr = ligne[i_tr]
                if i_cle is not None and not inverse:
                    cles[ligne[i_cle]] = tr or fr
                if fr and tr and fr != tr:
                    if inverse:
                        textes[tr] = fr
                    else:
                        textes[fr] = tr
    return textes, cles


def proteger(texte, javascript):
    """Guillemets typographiques : une traduction ne doit pas casser une chaîne JS ou un attribut HTML."""
    texte = texte.replace('"', "”")
    if javascript:
        texte = texte.replace("'", "’")
    return texte


def traduire_brut(contenu, textes, javascript):
    """Remplacement des textes dans une chaîne sans structure particulière."""
    for fr in sorted(textes, key=len, reverse=True):
        # Une espace du texte français vaut aussi pour une espace insécable (U+00A0).
        corps = "".join("[ \u00a0]" if c == " " else re.escape(c) for c in fr)
        motif = re.compile(r"(?<!\w)" + corps + r"(?!\w)")
        contenu = motif.sub(lambda m, t=proteger(textes[fr], javascript): t, contenu)
    return MARQUE.sub("Occitux", contenu)


# Un gabarit HTML/Jinja n'est traduit que là où un humain lit : les textes
# entre les balises, quelques attributs (title, placeholder, alt, aria-label),
# et les chaînes des blocs <script> (en mode JavaScript). Les expressions Jinja
# ({{ }}, {% %}, {# #}) et le reste des balises restent intacts.
JINJA = r"\{\{.*?\}\}|\{%.*?%\}|\{#.*?#\}"
SEGMENTS = re.compile(r"(?s)(" + JINJA + r"|<script\b.*?</script>|<style\b.*?</style>|<!--.*?-->|<[^>]*>)")
ATTRIBUTS = re.compile(r'\b(title|placeholder|alt|aria-label)=("[^"]*"|\'[^\']*\')')


def traduire_html(contenu, textes):
    def balise(b):
        if b.startswith("<script"):
            m = re.match(r"(?s)(<script\b[^>]*>)(.*)(</script>)", b)
            return m.group(1) + traduire_jinja(m.group(2), textes, True) + m.group(3) if m else b
        if b.startswith("<style") or b.startswith("<!--"):
            return b
        return ATTRIBUTS.sub(lambda m: m.group(1) + "=" + m.group(2)[0] + traduire_brut(m.group(2)[1:-1], textes, False) + m.group(2)[-1], b)

    morceaux = SEGMENTS.split(contenu)
    for i, m in enumerate(morceaux):
        if i % 2 == 0:
            morceaux[i] = traduire_brut(m, textes, False)
        elif m.startswith("{{") or m.startswith("{%") or m.startswith("{#"):
            pass
        else:
            morceaux[i] = balise(m)
    return "".join(morceaux)


def traduire_jinja(contenu, textes, javascript):
    """Texte sans balises (JavaScript, SQL…) : seules les expressions Jinja sont épargnées."""
    morceaux = re.split(r"(?s)(" + JINJA + r")", contenu)
    for i, m in enumerate(morceaux):
        if i % 2 == 0:
            morceaux[i] = traduire_brut(m, textes, javascript)
    return "".join(morceaux)


def traduire_texte(contenu, textes, javascript, html=False):
    if html:
        return traduire_html(contenu, textes)
    return traduire_jinja(contenu, textes, javascript)


def traduire_diapo(contenu, nom, cles, textes, javascript):
    """Diapositive du diaporama d'installation : titre et texte entiers."""
    titre = cles.get(f"diapo.{nom}.titre")
    texte = cles.get(f"diapo.{nom}.texte")
    if titre:
        contenu = re.sub(r'(<h1 class="slidetitle">).*?(</h1>)', lambda m: m.group(1) + titre + m.group(2), contenu, flags=re.S)
    if texte:
        contenu = re.sub(r'(<div class="text">).*?(</div>\s*</div>)',
                         lambda m: m.group(1) + "\n<div>\n<p>" + texte + "</p>\n" + m.group(2),
                         contenu, count=1, flags=re.S)
    return traduire_texte(contenu, textes, javascript, html=True)


def traduire_sqlite(base, textes):
    """Catégories du menu des élèves (table levels)."""
    con = sqlite3.connect(base)
    try:
        for colonne in ("name_level_one", "name_level_two"):
            for fr, tr in textes.items():
                con.execute(f"UPDATE levels SET {colonne} = ? WHERE {colonne} = ?", (tr, fr))
        con.commit()
    finally:
        con.close()


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--langue", choices=COLONNE, default="oc")
    p.add_argument("--textes", default="/usr/share/occitux/textes")
    p.add_argument("--diapo", metavar="NOM")
    p.add_argument("--sqlite", metavar="BASE")
    p.add_argument("--inverse", action="store_true", help="retour au français (désinstallation)")
    p.add_argument("--cle", metavar="CLAU", help="affiche le texte d'une clé")
    p.add_argument("source", nargs="?")
    p.add_argument("destination", nargs="?")
    a = p.parse_args()
    textes, cles = lire_tables(a.textes, COLONNE[a.langue], a.inverse)
    if a.cle:
        if a.cle not in cles:
            return 1
        print(cles[a.cle])
        return 0
    if a.sqlite:
        traduire_sqlite(a.sqlite, textes)
        return 0
    if not a.source or not a.destination:
        p.error("source et destination requises")
    with open(a.source, encoding="utf-8", errors="surrogateescape") as f:
        contenu = f.read()
    javascript = a.source.endswith(".js")
    html = a.source.endswith((".html", ".htm"))
    if a.diapo:
        contenu = traduire_diapo(contenu, a.diapo, cles, textes, javascript)
    else:
        contenu = traduire_texte(contenu, textes, javascript, html)
    tmp = a.destination + ".occitux-tmp"
    with open(tmp, "w", encoding="utf-8", errors="surrogateescape") as f:
        f.write(contenu)
    shutil.copymode(a.source, tmp)
    os.replace(tmp, a.destination)
    return 0


if __name__ == "__main__":
    sys.exit(main())
