# Formes conservées et limites de validation

Une forme non attestée dans le sens demandé ne devient pas béarnaise par ressemblance.
Les formes ci-dessous restent celles des catalogues occitans. Les cases vides signalent
une absence dans les paquets examinés. Aucune entrée n'est ajoutée pour combler cette absence.

## Notions du glossaire

| Notion | Forme conservée | Recherche et résultat |
|---|---|---|
| renommer | Renomenar | Corpus : renomenar (forme entière, 0 occurrences), renommer (côté français, 0 occurrences). Corpus : renomenar et renommer. Per Noste, renommer : sens réélire, pas changer le nom d'un fichier. Pas de choix technique attesté retenu. |
| désinstaller | desinstallar | Corpus : desinstallar (forme entière, 0 occurrences), désinstaller (côté français, 0 occurrences). Corpus : desinstallar et désinstaller. Consultation Per Noste désinstaller : aucun bloc de résultats exploitable. |
| préférences | preferéncias | Corpus : preferéncias (forme entière, 0 occurrences), préférences (côté français, 0 occurrences). Corpus : preferéncias et préférences. Per Noste préférence : preferéncia au singulier ; pluriel non attesté dans le corpus. Pas de différence retenue. |
| volume sonore | volum | Corpus : volume (forme entière, 5 occurrences), volume sonore (côté français, 0 occurrences). Corpus : volum, volume et volume sonore. Per Noste volume : volume dans les sens livre, scientifique ou ampleur ; emploi audio non établi. Conservation de Volum. |
| casque | Absente | Corpus : casco (forme entière, 0 occurrences), casque (côté français, 0 occurrences). Corpus : casco et casque. Per Noste casque : casco, sans précision permettant de distinguer casque protecteur et écouteurs. Forme source absente des catalogues examinés ; colonne languedocienne laissée vide. |
| serveur | servidor | Corpus : servidor (forme entière, 0 occurrences), serveur (côté français, 0 occurrences). Corpus : servidor et serveur. Per Noste serveur : pas d'entrée exactement homographe dans les résultats. |
| bravo | Crane | Corpus : bravo (forme entière, 0 occurrences), bravo (côté français, 0 occurrences). Corpus : bravo et bravo côté français. Per Noste bravo : aucune entrée exactement homographe. Recherche Wiktionnaire bravo gascon béarnais : aucun résultat probant. Crane conservé dans Tux Paint. |
| tampon | Tampon | Corpus : tampon (forme entière, 0 occurrences), tampon (côté français, 0 occurrences). Corpus : tampon et tampon. Per Noste tampon : bouchon, tampon ferroviaire, sagèth postal ; application à l'outil graphique non établie. |

## Flexions non introduites

Une attestation du singulier ne constitue pas ici une attestation littérale du pluriel.
Les formes suivantes n'ont aucune occurrence exacte dans le corpus. Elles ne sont pas
fabriquées automatiquement dans les PO ; les chaînes concernées restent en occitan.

| Source oc | Forme cherchée | Recherche |
|---|---|---|
| fenèstras | frinèstas | Mot entier côté occitan : 0 résultat. Singulier vérifié dans le glossaire. |
| gomas | gòmas | Mot entier côté occitan : 0 résultat. Singulier vérifié dans le glossaire. |
| bròssas | pincèus | Mot entier côté occitan : 0 résultat. Singulier vérifié dans le glossaire. |

## Chaînes conservées

229 chaînes ont des différences repérées mais ne sont pas livrées dans le delta.
Elles figurent individuellement dans [audit.md](audit.md) et [audit.csv](audit.csv),
avec leur clé exacte et leur motif : conjugaison, construction de phrase, pluriels gettext,
sens technique non établi, ou défaut des paramètres et raccourcis dans la source.
Le glossaire ne valide pas à lui seul la syntaxe de toutes les phrases qui emploient ses mots.

| Domaine | Chaînes conservées |
|---|---:|
| xfce4-panel | 38 |
| xfce4-session | 22 |
| xfdesktop | 28 |
| thunar | 100 |
| xfwm4 | 31 |
| tuxpaint | 2 |
| ristretto | 5 |
| xfce4-pulseaudio-plugin | 2 |
| lightdm-gtk-greeter | 1 |

## Variantes et sens à ne pas confondre

- `nòu` peut désigner neuf ou nouveau. Le mot de l'horloge n'est pas remplacé par `navèth`.
- `ret` est féminin dans les catalogues sources ; `hialat` est masculin. Un remplacement sans accord est écarté.
- `sens` peut être un nom ou signifier sans. `font` peut être source ou apparaître dans un contexte typographique.
- `son` peut être un nom, un possessif ou un verbe. L'entrée Per Noste son (audition) sert pour le son de l'ordinateur.
- Le corpus contient des citations languedociennes, notamment des passages narratifs en C038xx et des interfaces en C072xx. L'étiquette du fichier ne les rend pas béarnaises.
- Pour fenêtre, Per Noste distingue notamment `frinèsta`, des formes pyrénéennes `hrièsta` / `herièsta`, et des formes bigourdanes `hièstra` / `hiestra`. La forme commune retenue est aussi attestée dans une interface vidéo en C06017. Aucune de ces indications ne démontre une exclusivité ossaloise.

## Reproduire une recherche

```sh
python3 traductions/outils/corpus.py frinèstas --mot
python3 traductions/outils/corpus.py fenêtre --fr
python3 traductions/outils/dicodoc.py fenêtre
```

Le périmètre de livraison est un delta vérifié et conservateur, pas la certification intégrale
des traductions amont. Les chaînes différées restent un travail à terminer, explicitement visible.

# Tables de substitution du 23 octobre 2026

`primtuxmenu.csv`, `systeme.csv` et la colonne `occitan` d'`occitux.csv` sont des
substitutions texte exact → texte exact, sans gettext. Les formes ci-dessous ont été
livrées malgré une attestation incomplète ; elles sont à relire avant toute recette.
Les attestations retenues figurent dans `glossari.csv` (lignes datées 2026-10-23).

## Formes reprises d'un seul dictionnaire, sans occurrence dans le corpus ni les catalogues

| Notion | Forme | Colonne | Source unique et remarque |
|---|---|---|---|
| koala | coala | occitan, béarnais | Per Noste seul ; Laux sans entrée, aucun catalogue. |
| pieuvre | pofre / lagast | occitan / béarnais | Laux (pofre) et Per Noste (lagast) ; genre masculin dans les deux cas : « Poe lo pofre », « Poe lo lagast ». |
| caméléon | camaleon | occitan, béarnais | Laux et Per Noste ; aucun catalogue. |
| appuyer (sur Entrée) | prémer | béarnais | Per Noste, sens presser. `quichar` n'est attesté qu'en languedocien (C04861, catalogues oc). |
| phase | fasi | béarnais | Per Noste ; les catalogues oc emploient `fasa`. |
| dysfonctionnement | disfoncionament | occitan, béarnais | Per Noste seul ; Laux sans entrée. Forme languedocienne identique par défaut. |
| parental | pairau | béarnais | Per Noste, sens « relatif au père et à la mère ». Le languedocien `parental` n'est ni dans Laux ni dans les catalogues ; `Contraròtle parental` reste une construction. |
| flouté | fosc | occitan, béarnais | Per Noste et Laux donnent `fosc` pour flou ; flouter n'a pas d'entrée. |
| signalement | senhalada | béarnais | Per Noste, « action de signaler ». Le languedocien `senhalament` vient du catalogue oc d'apport. |
| forge (logicielle) | farga / harga | occitan / béarnais | Laux et Per Noste au sens d'atelier ; l'emploi pour une forge logicielle est métaphorique, comme en français. |
| jeton (token) | geton | occitan, béarnais | Per Noste et Laux ; le sens informatique n'est attesté que dans le catalogue oc de Linux-PAM. |
| ticket | ticket | occitan, béarnais | Mot conservé tel quel (jargon de la forge). Laux et le catalogue oc de sudoers donnent `tiquet`. |
| agencé, fluidité, inédit | agençat, fluiditat, inedit | occitan, béarnais | Dictionnaires seuls pour agençar et fluiditat ; inedit attesté en C07842. |
| fonctionnalité | foncionalitat | occitan | Catalogues oc (cinder, nova, notificationhelper) ; Laux sans entrée. |
| plus tard | mei tard | béarnais | Composé mei + tard ; le corpus n'offre que la forme bigourdane `ath mes tard` (C03002), non retenue. |

## Flexions et constructions non attestées littéralement

Les tables contiennent des phrases entières ; participes et accords ont été formés
sur des lemmes attestés mais n'ont pas tous une occurrence exacte : `indicada`,
`constatadas`, `classadas`, `adaptats`, `dedicada`, `accessiblas`, `suprimits`,
`actualizats`, `disponiblas`, `rapida`, `completa`, `suplementària`, `materiaus`,
`leugèrs`, `inedita`, `simplificat`, `qui an miat`, `que desfaça`, `escafa`.
Les tournures `que deu`, `qu'ei`, `que cau`, `que's pòden` suivent l'énonciatif des
phrases affirmatives (README) ; les énumérations et infinitifs restent sans `que`.
Le mot `reproductibles` n'a pas d'équivalent attesté en gascon : la phrase béarnaise
dit « se possible de tornar har » (glossaire refaire).

## Choix à connaître

- `Session` : le catalogue XFCE oc dit `sesilha`, LibreOffice oc dit `session`. La
  colonne occitane suit XFCE (`Sesilha :`, `sesilha d'escolan`), la béarnaise garde
  `session` (glossaire). Si l'ISO n'affiche pas XFCE en occitan, revoir ce choix.
- `Redémarrer` : `Reaviar` (LibreOffice, GRUB, friendly-recovery) ; XFCE oc dit
  `Reamodar`. Une seule forme a été retenue pour toutes les tables.
- `Bienvenue` : `Benvenguda` (oc) ; `Benvienguda` (glossaire, Per Noste). Le corpus
  atteste aussi `planvenguda` (C03048), également donnée par Per Noste.
- `Explorer le monde` : `mond` en oc (catalogues), `monde` en béarnais (C07422) ; Per
  Noste admet les deux.
- `Grandeur et mesure` est traduit au singulier, comme la source PrimTux, et non
  « Grandors e mesuras ».
- `Outils du professeur` : `professor` (source), pas `regent` (C06216, « enseignant »).
- `Lecture-compréhension` : `compreneson` (corpus C08153) ; Per Noste donne d'abord
  `comprenença`.
- `Descriptif` et `Description` donnent tous deux `Descripcion` : deux chaînes
  françaises distinctes, aucune collision de substitution.
- `Ex : Au jardin, Achats…` est un exemple de titre ; il est rendu par un exemple de
  même nature (`Al jardin` / `Au casau`), pas par une traduction littérale.
- La chaîne `est important ici d` (top_bar.html) est un fragment coupé ; elle n'est
  pas dans la table, une substitution partielle pouvant casser le gabarit.
- Les fragments `L'objet concerné de type \` et `La gravité pour une anomalie de type \`
  conservent la barre oblique inverse finale de la source Python.
- Dans `systeme.csv`, la colonne `frances` des diapositives est déjà adaptée à Occitux
  (nom, Calandretas, lien de documentation) : ce n'est pas le texte PrimTux d'origine.
  La balise `<a href=…>` de `diapo.gethelp.texte` est conservée sans fermeture, comme
  dans la source, et pointe vers https://github.com/GMS64260/occitux.
- `Désactiver le splash` : `l'imatge de presentacion`, comme GRUB oc ; `splash` n'a
  pas d'équivalent attesté.

## Reproduire une recherche

```sh
python3 traductions/outils/dicodoc.py --dic LAUS géométrie
python3 traductions/outils/dicodoc.py koala
python3 traductions/outils/corpus.py escolans --mot
python3 -I traductions/outils/verifier_csv.py
```
