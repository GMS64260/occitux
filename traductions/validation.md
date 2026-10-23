# Contrôles du 21 octobre 2026

Sur les versions identifiées dans `provenance.json`, avec `polib==1.2.0` et les
outils gettext de la machine de travail :

- Corpus : empreinte MD5 conforme et 8 552 enregistrements.
- Glossaire : 316 notions, 308 attestées, huit réserves explicites.
- Catalogues : 855 entrées différentes de leur source, réparties dans neuf
  domaines non vides. Le dixième fichier, `lightdm.po`, ne contient que l'en-tête,
  car le catalogue source ne fournit aucune chaîne.
- `msgfmt --check -o /dev/null` : succès pour les dix fichiers PO.
- Paramètres, raccourcis, balises, clés et encodage : contrôles réussis.
- Reformulations explicites : aucune substitution lexicale restante parmi les
  règles retenues du glossaire.
- Repli testé avec GNU `gettext` et `LANGUAGE=oc_FR@gascon:oc:fr` : neuf essais
  béarnais, neuf essais occitans et six essais français réussis.
- Textes propres à Occitux : 15 clés, chacune accompagnée de ses sources ;
  variables shell et paramètres conservés.

Les essais de repli ne couvrent que des entrées témoins, pas toutes les branches
de chaque logiciel. Ils utilisent un répertoire de locale local à
`traductions/construction/` et ne modifient pas la configuration système.

La validation automatique de présence lexicale porte sur les mots nouveaux,
pas sur une recertification des mots conservés depuis les catalogues amont.
Une concordance doit toujours être lue dans son contexte. Les commentaires des
PO renvoient aux choix du glossaire ou aux attestations complémentaires.

229 chaînes présentant des différences repérées sont différées, avec leurs
motifs dans `audit.md` et `audit.csv`. Elles ne sont pas injectées dans le delta.
Sept notions non validées gardent leur forme source ; une huitième n'apparaît
pas dans les catalogues. Trois flexions non attestées sont aussi signalées dans
`incertituds.md`. Aucun particularisme n'est attribué à l'Ossau sans preuve locale.

Ce rapport ne vaut ni validation linguistique intégrale ni recette sur l'ISO
PrimTux 9. La branche reste un brouillon avec un périmètre de livraison et des
réserves explicites. Les commandes de reproduction figurent dans `README.md`.

# Contrôles du 23 octobre 2026

Tables de substitution pour le menu des élèves (`primtuxmenu.csv`), l'écran de
connexion, le lanceur, la fin d'installation et le diaporama (`systeme.csv`), et
textes propres au projet (`occitux.csv`, désormais `clau;frances;occitan;bearnes`).

- Sources consultées : corpus Lo Congrès v1.0 (MD5 conforme, 8 552 enregistrements) ;
  Dicodòc, Per Noste (gascon) et Laux (languedocien), mot par mot ; catalogues oc
  d'Ubuntu 24.04 : `language-pack-oc-base` 1:24.04+20260905 (248 MO) et
  `libreoffice-l10n-oc` 4:24.2.7-0ubuntu0.24.04.7 (33 MO), décompilés avec `msgunfmt`,
  hors du dépôt (`traductions/sources/`, ignoré par Git).
- `primtuxmenu.csv` : 128 chaînes françaises traduites sur les 145 chaînes uniques du
  relevé. 17 ne sont volontairement pas dans la table : noms propres (Jerry, Koda, Léon,
  Poe, Debian, Url), identifiants techniques (`application`, `error`, `feature`,
  `suggestion`, `system`, `nom@example.com`, `accessories`, `emc`, `languages`,
  `sciences`) et un fragment coupé (`est important ici d`). Aucune chaîne manquante,
  aucune chaîne hors relevé.
- `systeme.csv` : 33 clés (12 écran de connexion, 2 lanceur, 2 fin d'installation,
  16 titres et textes du diaporama, plus `connexion.bienvenue_court`).
- `occitux.csv` : 21 clés, 15 anciennes traduites en occitan languedocien sans changer
  la colonne béarnaise, 6 nouvelles ; `occitux-sources.csv` complété pour les 6.
- Glossaire : 485 notions, dont 169 ajoutées ce jour avec leurs attestations (corpus
  ou Dicodòc), 477 attestées, 8 réserves inchangées. Ces lignes ont été ajoutées à la
  main : `outils/glossaire.py` ne les régénère pas encore.
- `outils/verifier_csv.py` : encodage, en-têtes, colonnes, doublons, cases vides,
  conservation des variables `{…}`, `{{…}}`, `$VAR`, `${…}` (texte de remplacement
  des substitutions Bash exclu), entités `&nbsp;`, balises, espaces finaux, noms
  invariants, et absence de « PrimTux » résiduel hors de l'expression « PrimTux en
  occitan ». Résultat : les trois tables passent. Un essai avec quatre défauts
  plantés (variable renommée, entité perdue, PrimTux conservé, doublon) les détecte.
- `outils/dicodoc.py` accepte `--dic` (PNST par défaut, LAUS pour le languedocien).

Limites : les tables sont bien formées, non validées linguistiquement. Les formes
reprises d'un seul dictionnaire, les flexions sans occurrence exacte et les choix de
cohérence (sesilha, Reaviar, Benvienguda, mond/monde) sont listés dans
`incertituds.md`. Aucune chaîne n'a été testée dans l'application : la casse, les
espaces insécables et les coupures de gabarit restent à vérifier à l'injection.
