# Traductions béarnaises d'Occitux

Référence de travail en graphie classique, pour la Calandreta de Lys. Le glossaire
choisit une formulation impersonnelle : actions à l'infinitif, demandes courtes,
sans alternance entre tutoiement et vouvoiement. L'énonciatif `que` appartient aux
phrases affirmatives, pas aux noms de menus ni aux infinitifs.

`glossari.csv` est un CSV UTF-8 séparé par des points-virgules. Ses quatre premières
lignes, préfixées par `#`, exposent les conventions. `estat=conserve` signifie que
la forme occitane d'origine est conservée, sans certification béarnaise. Une case
vide signifie une absence de donnée, jamais une équivalence dialectale prouvée.
Les colonnes `ossau` et `source_ossau` sont réservées aux attestations précisément
localisées : une indication pyrénéenne peut intéresser le Béarn, mais ne suffit
pas à identifier une particularité ossaloise.

## Sources et attribution

[Aure Séguier et Lo Congrès, *Lo Congrès websites Corpus*, version 1.0,
20 juin 2024](https://doi.org/10.5281/zenodo.12192029), sous
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Fichier
`oc-gascon-grclass_fr.csv`, 8 552 entrées. Les identifiants `C00001` à `C08552`
désignent les enregistrements, pas nécessairement les lignes physiques : certains
contiennent des retours à la ligne. Les extraits du glossaire sont sélectionnés,
parfois tronqués, et la casse des lemmes est normalisée. Les traductions composées
sont signalées comme telles. La présence dans ce corpus ne dispense pas de lire
le contexte : il contient notamment des citations dans d'autres variétés.

[Dicodòc](https://dicodoc.eu/oc/diccionaris), dictionnaire **Per Noste (gascon)**,
Miquèu Grosclaude, Gilabèrt Nariòo et Patric Guilhemjoan : consultations mot par mot
le 21 octobre 2026. Tous droits réservés. Seuls les choix lexicaux et les liens
vers les entrées consultées sont consignés ; aucune copie des définitions ou de
la base du dictionnaire n'est distribuée. Une équivalence dans un autre sens
ne constitue pas une preuve du sens informatique.

Les formes occitanes sources proviennent des paquets **Ubuntu 24.04 Noble**,
extraits sans installation sur la machine. Les catalogues des logiciels visés
ne sont pas dans `language-pack-oc-base` dans la version téléchargée : ils sont
livrés dans les paquets des applications. Le paquet de langue complète le
glossaire pour les notions absentes de ces applications. `provenance.json`
identifie versions, chemins, empreintes et date de collecte. Les crédits des
traducteurs d'origine sont conservés dans les en-têtes des PO adaptés ; les
licences des logiciels restent applicables à leurs catalogues. Le corpus et ses
extraits gardent leur attribution CC BY 4.0.

LightDM et son écran d'accueil ont des domaines différents. Le catalogue
`lightdm` fourni est vide ; `lightdm-gtk-greeter` est audité en complément pour
couvrir les libellés de connexion. Le greeter réellement utilisé par l'ISO reste
à vérifier lors de l'intégration : un autre greeter utilise un autre domaine.

## Reproduire la collecte et les recherches

Depuis la racine du dépôt, avec Python 3, `gettext`, `dpkg-deb`, `curl`, APT et
`python3-venv` :

```sh
mkdir -p traductions/sources
curl -fL 'https://zenodo.org/records/12192029/files/oc-gascon-grclass_fr.csv?download=1' -o traductions/sources/oc-gascon-grclass_fr.csv
cd traductions/sources
apt-get download language-pack-oc-base language-pack-fr-base xfce4-panel xfce4-session xfdesktop4-data thunar-data xfwm4 tuxpaint-data lightdm ristretto xfce4-pulseaudio-plugin lightdm-gtk-greeter
cd ../..
python3 -m venv traductions/sources/venv
traductions/sources/venv/bin/pip install polib==1.2.0
python3 traductions/outils/inventorier.py
python3 traductions/outils/corpus.py fichèr --mot
python3 traductions/outils/corpus.py clavier --fr
python3 traductions/outils/corpus.py --id C06017
python3 traductions/outils/dicodoc.py souris
```

APT télécharge les versions proposées au moment de la commande. Pour reproduire
strictement cette collecte, utiliser `paquet=version` avec les versions de
`provenance.json`, et contrôler les SHA-256. Si une version n'est plus proposée,
la comparaison avec un nouveau catalogue doit être refaite.

`outils/examiner.py` affiche des concordances à examiner. Il ne certifie aucune
traduction. `outils/termes.csv` conserve les candidats de recherche, dont certains
ont été rejetés ; ce fichier ne doit pas être utilisé comme glossaire de livraison.
`outils/decisions.json` consigne les corrections, sources choisies et refus après
examen. `outils/glossaire.py` assemble le glossaire depuis ces choix.

Les téléchargements, extractions et fichiers de construction sont ignorés par
`traductions/.gitignore`. Aucun fichier système n'est modifié par ces outils.

## Catalogues partiels et repli

Les fichiers `gascon/*.po` ne doivent **pas écraser directement** les MO occitans
installés. Gettext ne fusionne pas deux fichiers `oc/LC_MESSAGES/domaine.mo`
présents dans deux répertoires. Avec `LANGUAGE=oc:fr`, remplacer le catalogue
occitan par un delta ferait perdre les traductions occitanes absentes du delta.

L'intégration doit fusionner les entrées du delta avec le catalogue `oc` de la
version installée, en donnant priorité aux entrées béarnaises, puis compiler le
résultat. Le repli français reste assuré par `LANGUAGE=oc:fr`. L'en-tête des PO
reste `Language: oc`. L'intégration au paquet est hors de cette branche ; les
outils de construction locaux n'écrivent que dans `traductions/construction/`.

Les expressions et formes non vérifiées restent dans le catalogue source et
sont signalées dans l'audit ou dans `incertituds.md`. Une compilation réussie
valide la structure gettext, pas à elle seule la langue.
