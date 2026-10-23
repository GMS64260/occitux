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
