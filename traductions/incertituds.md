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
