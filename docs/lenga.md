# La question de la langue

## Un seul « occitan » pour le système

Linux connaît une langue occitane, `oc` (paramètres régionaux `oc_FR.UTF-8`), sans variante. Les traductions des logiciels sont publiées sous ce code unique, sans dire si elles sont en languedocien, en gascon, en provençal ou en limousin. Dans les faits, elles sont surtout en **languedocien**.

Pour une Calandreta gasconne ou béarnaise, l'interface est donc dans un occitan qui n'est pas tout à fait celui de la classe. C'est aux regents de juger si c'est gênant pour des élèves :

- **accepter le languedocien** pour les menus : c'est ce que fait Occitux par défaut (`LANGUE=oc`) ;
- **garder l'interface en français** (`LANGUE=fr`) et réserver l'occitan aux contenus et aux activités ;
- **passer en béarnais** (`LANGUE=bearnes`) : Occitux installe ses propres traductions béarnaises (`traductions/gascon/`, rendues visibles dans `/usr/share/locale/oc@gascon`). Un logiciel les utilise d'abord, puis retombe sur l'occitan pour ce qu'elles ne couvrent pas, puis sur le français. On peut donc traduire en béarnais logiciel par logiciel, en commençant par ce que les enfants voient le plus, sans attendre que tout soit fait.

## Où en sont les traductions (octobre 2026)

| Logiciel | Occitan |
|---|---|
| Bureau GNOME 51 | environ 90 % de l'interface |
| Bureau XFCE | partiel |
| Firefox | traduit (paquet `firefox-locale-oc`, fourni par Mint) |
| LibreOffice | interface (`libreoffice-l10n-oc`) et dictionnaire (`hunspell-oc`, languedocien) |
| Menu PrimTux | aucune : le menu n'est pas encore traduisible |

Les traductions se font sur les plateformes de chaque projet : [GNOME](https://l10n.gnome.org/languages/oc), Transifex pour XFCE, Pontoon pour Firefox, Weblate pour LibreOffice. L'équipe occitane est [Tot en òc](http://www.totenoc.eu).

## Le correcteur gascon de Lo Congrès

Lo Congrès propose des correcteurs gascon et languedocien sur [dicodoc.eu](https://dicodoc.eu/fr/tutoriels), pour LibreOffice, Firefox et Chrome. Ils sont gratuits, mais leurs conditions d'utilisation interdisent la copie et la redistribution : **Occitux ne peut pas les inclure** sans l'accord de Lo Congrès.

En attendant, on peut les installer à la main sur chaque PC, depuis LibreOffice (*Outils → Gestionnaire des extensions*) avec le fichier `.oxt` gascon. Demander à Lo Congrès une licence libre pour ces correcteurs est dans la [feuille de route](feuille-de-route.md).

## Les traductions occitanes et l'élagage de PrimTux

PrimTux règle l'outil `localepurge` pour que les paquets n'installent que leurs traductions françaises : c'est une économie de place. Sans précaution, chaque mise à jour d'un logiciel effacerait donc sa traduction occitane, et le PC repasserait en français petit à petit.

Occitux ajoute `/etc/dpkg/dpkg.cfg.d/51occitux-langues`, qui garde les traductions occitanes et béarnaises lors des mises à jour. Les catalogues béarnais d'Occitux sont livrés dans `/usr/share/occitux/locale/` et reliés à `/usr/share/locale/oc@gascon` par `occitux-config`.

Limite : sur un PrimTux installé avant Occitux et déjà mis à jour, les traductions occitanes effacées par ces mises à jour ne reviennent qu'à la prochaine mise à jour de chaque logiciel.
