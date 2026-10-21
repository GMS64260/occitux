#!/usr/bin/env python3
"""Construire un delta prudent et son audit depuis le glossaire sourcé.

Une substitution lexicale ne valide pas une phrase conjuguée : ces phrases
restent dans la liste à vérifier, sauf traduction explicite relue.
"""
import copy
import csv
import json
import re
from collections import Counter
import polib
from corpus import RACINE as R, lire, normaliser
from glossaire import catalogues, lire_glossaire, limite_mot
from inventorier import DOMAINES

PRINTF = re.compile(r"%(?:\d+\$)?[-+#0 ']*(?:\*|\d+)?(?:\.(?:\*|\d+))?(?:hh|ll|[hlLjzt])?[diouxXeEfFgGaAcspn%]")
PROTEGE = re.compile(r"<[^>]*>|\{[^}]*\}|%(?:\d+\$)?[-+#0 ']*(?:\*|\d+)?(?:\.(?:\*|\d+))?(?:hh|ll|[hlLjzt])?[diouxXeEfFgGaAcspn%]")
PHRASE = re.compile(r"\b(?:es|èsser|son|sètz|soi|som|avètz|avèm|ai|pòt|pòdon|podètz|volètz|vòstre|vòstra|vòstres|vòstras|vos|vòu|cal|cau|foguèt|èra|èran|aviá|aqueste|aquesta|aquestes|aquestas|existís|existisson|conten|crèa|aficha|pega|suprimís|correspondon|seguís|seràn|venon|siá|fasent|quand|quichatz|dempuèi)\b|\b(?:a|an|fa) (?:pas|fracassat|pogut)|\b\w+(?:atz|ètz|issètz)\b|[.!?]$", re.I)

# Notions non ambiguës dans un libellé d'interface. Per/entà, cap/nat,
# sens/shens, font/hont et les autres homographes sont traités séparément.
CLES = """ouvrir fermer ajouter effacer dossier fichier texte logiciel ordinateur fenetre
session utilisateur clavier souris imprimante microphone haut_parleur
deverrouiller verrouiller recevoir envoyer redemarrer eteindre remplir
voir lire ecrire faire mettre vider sauvegarder nouveau nouvelle autres meme
avec dans du des sur_le sur_les au aux une ici jamais encore deja plus moins
haut droite derriere dessous premier premiere dernier derniere petit grand
hauteur ordre contenu donnees jour aujourdhui hier midi nuit calendrier
rouge bleu violet fond gomme normal general personnel manuel libre actuel
travail reinitialiser refaire accord modele rapide difficile enregistrer police inconnu
ensuite comme dessous_ici tres session_pluriel vide modifier chercher video panneau outil""".split()

FLEXIONS = [
    ("fichièrs", "fichèrs", "fichier", "C00956"),
    ("dorsièrs", "dossièrs", "dossier", "C03179"),
    ("repertòris", "dossièrs", "dossier", "C03179"),
    ("clavièrs", "clavèrs", "clavier", "C07562"),
    ("logicials", "logiciaus", "logiciel", "C04225"),
    ("utilizaires", "utilizators", "utilisateur", "C07994"),
    ("generals", "generaus", "general", "C07327"),
    ("personals", "personaus", "personnel", "C06510"),
    ("novèls", "navèths", "nouveau", "C05885"),
    ("novèlas", "navèras", "nouvelle", "C07887"),
    ("nòvas", "navèras", "nouvelle", "C07887"),
    ("autras", "autas", "autre", "C05702"),
    ("oras", "òras", "heure", "C06599"),
    ("jorns", "dias", "jour", "C08095"),
    ("personala", "personau", "personnel", "C08411"),
    ("personalas", "personaus", "personnel", "C06510"),
    ("generala", "generau", "general", "C03230"),
    ("darrièras", "darrèras", "derniere", "C05191"),
    ("modèls", "modèles", "modele", "C00195"),
    ("dobertura", "obertura", "ouvrir", "C06047"),
    ("vidèos", "videos", "video", "C04304"),
    ("panèls", "panèus", "panneau", "C08204"),
    ("tablèus de bòrd", "panèus", "panneau", "C08204"),
    ("espleches", "utís", "outil", "C01016"),
]

# Ici la forme plurielle nouvelle n'est attestée dans aucune source consultée.
# On conserve toute la chaîne, au lieu de fabriquer un paradigme.
FLEXIONS_DIFFEREES = {"fenèstras": "frinèstas", "gomas": "gòmas", "bròssas": "pincèus"}


def formats(s):
    qt = re.compile(r"%\d+(?![\d$.a-zA-Z])")
    rest = qt.sub("", s)
    return Counter(qt.findall(s) + PRINTF.findall(rest) + re.findall(r"\{[^{}]*\}", s)
                   + re.findall(r"%[A-Za-z]", PRINTF.sub("", rest)))


def accelerateurs(s):
    return (len(re.findall(r"(?<!_)_(?!_)", s)), len(re.findall(r"(?<!&)&(?![&#a-zA-Z0-9]+;|&)", s)))


def casse(source, cible):
    if source.isupper():
        return cible.upper()
    if source[:1].isupper():
        return cible[:1].upper() + cible[1:]
    return cible


def remplacer_mot(s, ancien, nouveau):
    # Autoriser un raccourci dans le mot et conserver sa lettre si elle existe.
    motif = r"(?<![^\W_])" + "_?".join(re.escape(c) for c in ancien) + r"(?![^\W_])"
    def repl(m):
        source = m[0]
        # Un soulignement interne n'est pas une frontière de mot : O_metre
        # ne doit jamais devenir O_méter par la règle metre -> méter.
        if m.start() >= 2 and m.string[m.start() - 1] == "_" and m.string[m.start() - 2].isalnum():
            return source
        if m.end() + 1 < len(m.string) and m.string[m.end()] == "_" and m.string[m.end() + 1].isalnum():
            return source
        cible = casse(source.replace("_", ""), nouveau)
        if "_" in source:
            pos = source.index("_")
            lettre = source[pos + 1:pos + 2].casefold()
            nouvelle_pos = cible.casefold().find(lettre)
            if nouvelle_pos < 0:
                nouvelle_pos = 0
            cible = cible[:nouvelle_pos] + "_" + cible[nouvelle_pos:]
        return cible
    morceaux = []
    dernier = 0
    for m in PROTEGE.finditer(s):
        morceaux.append(re.sub(motif, repl, s[dernier:m.start()], flags=re.I))
        morceaux.append(m[0])
        dernier = m.end()
    morceaux.append(re.sub(motif, repl, s[dernier:], flags=re.I))
    return "".join(morceaux)


def regles(glossaire):
    definitions = {r["clau"]: r for r in glossaire}
    candidats = list(csv.DictReader((R / "outils/termes.csv").open(), delimiter=";"))
    regles = []
    for t in candidats:
        r = definitions[t["clau"]]
        if t["clau"] not in CLES or r["estat"] != "atteste":
            continue
        for ancien in t["formes_oc"].split("|"):
            if ancien != r["bearnes"]:
                regles.append((ancien, r["bearnes"], r["clau"], r["source_forme"]))
    # Termes grammaticaux attestés, appliqués dans des groupes nominaux.
    regles += [("autra", "auta", "autre", "C00011"),
               ("autre", "aute", "autre", definitions["autre"]["source_forme"]),
               ("totes", "tots", "tous", "C06780"),
               ("ora", "òra", "heure", "C08080"),
               ("normala", "normau", "normal", definitions["normal"]["source_forme"]),
               ("actuala", "actuau", "actuel", definitions["actuel"]["source_forme"])]
    return sorted(regles + FLEXIONS, key=lambda r: -len(r[0]))


def manuelles():
    return json.loads((R / "outils/phrases.json").read_text()) if (R / "outils/phrases.json").exists() else []


def adapter(chaine, msgid, fr, regles):
    termes, sources = [], []
    nouveau = chaine
    for ancien, cible, notion, source in regles:
        if ancien == "nòu" and not re.search(r"\bnew\b", msgid, re.I):
            continue  # neuf (nombre) et nouveau sont homographes en occitan source.
        remplace = remplacer_mot(nouveau, ancien, cible)
        if remplace != nouveau:
            termes.append(notion)
            sources.append(source)
            nouveau = remplace
    # Les homonymes ne se résolvent pas par un remplacement sans contexte.
    for fr_mot, ancien, notion in [("sans", "sens", "sans"), ("source", "font", "source"),
            ("pour le", "pel", "pour_le"), ("pour les", "pels", "pour_les"),
            ("par le", "pel", "par_le"), ("par les", "pels", "par_les")]:
        if limite_mot(fr_mot).search(normaliser(fr)):
            gloss = next(r for r in lire_glossaire() if r["clau"] == notion)
            remplace = remplacer_mot(nouveau, ancien, gloss["bearnes"])
            if remplace != nouveau:
                termes.append(notion)
                sources.append(gloss["source_forme"])
                nouveau = remplace
    nouveau = re.sub(r"\bde (?=(_?o_?b_?r_?i_?r|enviar)\b)", "d'", nouveau)
    return nouveau, sorted(set(termes)), sorted(set(sources))


def md(s):
    return s.replace("|", "\\|").replace("\n", "<br>").replace("—", "-")


def main():
    glossaire = lire_glossaire()
    reg = regles(glossaire)
    c = {r["id"]: r for r in lire()}
    for _, cible, _, source in FLEXIONS:
        assert limite_mot(cible).search(normaliser(c[source]["oc"])), (cible, source)
    originals, francais = catalogues(), catalogues("fr")
    manuels = {(r["domaine"], r["msgid"]): r for r in manuelles()}
    exclusions = json.loads((R / "outils/exclusions.json").read_text()) if (R / "outils/exclusions.json").exists() else {}
    audit, stats = [], []
    (R / "gascon").mkdir(exist_ok=True)
    for d in DOMAINES:
        po = polib.POFile(wrapwidth=88)
        po.header = f"Adaptation lexicale béarnaise pour Occitux.\nSource : paquet Ubuntu, voir ../provenance.json.\nCrédits amont conservés ci-dessous.\n{originals[d].header}"
        po.metadata = dict(originals[d].metadata)
        po.metadata["X-Original-Last-Translator"] = po.metadata.get("Last-Translator", "Catalogue source vide")
        po.metadata.update({"Project-Id-Version": f"Occitux {d}", "Language": "oc",
            "MIME-Version": "1.0", "Content-Type": "text/plain; charset=UTF-8",
            "Content-Transfer-Encoding": "8bit", "PO-Revision-Date": "2026-10-21 12:00+0200",
            "Plural-Forms": "nplurals=2; plural=(n > 1);",
            "X-Occitux-Glossaire": "../glossari.csv", "X-Occitux-Delta": "yes"})
        po.metadata["Last-Translator"] = "Projet Occitux"
        po.metadata.setdefault("Language-Team", "Occitux - occitan gascon")
        po.metadata.setdefault("Report-Msgid-Bugs-To", "https://github.com/GMS64260/occitux/issues")
        n_report = 0
        for e in originals[d]:
            f = francais[d].find(e.msgid, msgctxt=e.msgctxt)
            fr = f.msgstr if f else ""
            traduction, termes, sources = adapter(e.msgstr, e.msgid, fr, reg)
            raison = ""
            manuel = manuels.get((d, e.msgid))
            if manuel:
                traduction, termes, sources = manuel["bearnes"], manuel["termes"], manuel["sources"]
            elif traduction != e.msgstr:
                if e.msgid in exclusions.get(d, []):
                    raison = "Sens, accord ou terminologie technique de la source non validés."
                elif e.msgid_plural:
                    raison = "Pluriel gettext : phrase à valider intégralement."
                elif PHRASE.search(e.msgstr.replace("_", "").rstrip("….")):
                    raison = "Phrase conjuguée, adresse personnelle ou phrase complète à valider."
                elif any(limite_mot(m).search(normaliser(e.msgstr.replace("_", ""))) for m in FLEXIONS_DIFFEREES):
                    raison = "Flexion nouvelle non attestée dans les sources consultées."
                elif len(e.msgstr) > 160 or "http" in e.msgstr or " --" in e.msgstr:
                    raison = "Contexte technique ou long : relecture intégrale nécessaire."
            if traduction != e.msgstr and not raison:
                if formats(traduction) != formats(e.msgid):
                    raison = "Paramètres de substitution divergents dans la source : correction complète nécessaire."
                elif accelerateurs(traduction) != accelerateurs(e.msgid):
                    raison = "Nombre de raccourcis divergent dans la source : correction contextualisée nécessaire."
            if traduction == e.msgstr and not e.msgid_plural:
                continue
            if e.msgid_plural:
                formes = [e.msgstr_plural[k] for k in sorted(e.msgstr_plural)]
                if not any(adapter(s, e.msgid, fr, reg)[0] != s for s in formes):
                    continue
                raison = "Pluriel gettext : validation de toutes les formes requise."
                source_texte = " / ".join(formes)
            else:
                source_texte = e.msgstr
            statut = "differe" if raison else "delta"
            audit.append(dict(domaine=d, msgctxt=e.msgctxt or "", msgid=e.msgid,
                frances=fr, occitan=source_texte, bearnes=traduction if not raison else "",
                statut=statut, termes=" | ".join(termes), sources=" | ".join(sources), motif=raison))
            if raison:
                n_report += 1
                continue
            entree = copy.deepcopy(e)
            entree.msgstr = traduction
            entree.comment = "Glossaire : " + ", ".join(termes) + "\nAttestations : " + " ; ".join(sources)
            if PRINTF.search(e.msgid) and not re.search(r"%\d+(?![\d$.a-zA-Z])", e.msgid):
                entree.flags = sorted(set(entree.flags) | {"c-format"})
            po.append(entree)
        po.save(str(R / "gascon" / f"{d}.po"))
        stats.append(dict(domaine=d, source=len(originals[d]), delta=len(po), differe=n_report))
    with (R / "audit.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(audit[0]), delimiter=";", lineterminator="\n")
        w.writeheader()
        w.writerows(audit)
    texte = ["# Audit des catalogues occitans d'Ubuntu 24.04", "",
        "Les catalogues décompilés par `msgunfmt` sont identifiés dans [provenance.json](provenance.json).",
        "L'audit lexical parcourt toutes leurs entrées. Il distingue les différences intégrées",
        "des chaînes conservées en attente de validation complète. Il ne certifie pas les chaînes",
        "sans différence repérée. [audit.csv](audit.csv) fournit les clés et contextes exacts.", "",
        "| Domaine | Entrées oc sources | Delta béarnais | Différences différées |", "|---|---:|---:|---:|"]
    for s in stats:
        texte.append(f"| {s['domaine']} | {s['source']} | {s['delta']} | {s['differe']} |")
    texte += ["", "Le domaine `lightdm` est vide dans le paquet ; les libellés de connexion se trouvent",
              "dans `lightdm-gtk-greeter`, ajouté à l'audit. Aucune chaîne n'est inventée dans le domaine vide.", "",
              "Les deltas ne remplacent pas directement les MO installés : voir le repli dans [README.md](README.md).", ""]
    for d in DOMAINES:
        texte += [f"## {d}", "", "| Clé source | Occitan livré | Béarnais retenu ou motif de conservation | Glossaire |",
                  "|---|---|---|---|"]
        for r in audit:
            if r["domaine"] == d:
                texte.append("| " + " | ".join(md(s) for s in [r["msgid"], r["occitan"], r["bearnes"] or "Conservé : " + r["motif"], r["termes"]]) + " |")
        if not originals[d]:
            texte.append("| Catalogue vide | | Aucun remplacement | |")
        texte.append("")
    (R / "audit.md").write_text("\n".join(texte), encoding="utf-8")
    (R / "construction").mkdir(exist_ok=True)
    (R / "construction/statistiques.json").write_text(json.dumps(stats, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(stats, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
