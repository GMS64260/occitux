# Occitux

**PrimTux en occitan, pour les Calandretas.**
*PrimTux en occitan, per las Calandretas.*

Occitux est une variante de [PrimTux](https://primtux.fr), la distribution Linux faite par des enseignants pour l'école primaire. Elle ajoute une couche occitane à PrimTux, sans la modifier : interface, clavier, logiciels et dictionnaire en occitan, plus des réglages adaptés à une école tenue par des bénévoles.

Occitux vise les PC des Calandretas, souvent reconditionnés. Les besoins sont donc ceux de PrimTux 9 : PC 64 bits de 2010 ou plus récent, 2 Go de mémoire (4 Go recommandés), 40 Go de disque (SSD conseillé), Secure Boot désactivé.

> **État : version 0.1, en construction.** Le paquet est testé automatiquement sur Ubuntu 24.04, la base de Linux Mint 22.3. L'ISO complète n'a pas encore été essayée sur un vrai PC d'école.

## Ce qu'apporte Occitux

| | |
|---|---|
| **Langue** | Interface en occitan (`oc_FR`). Ce qui n'est pas traduit s'affiche en français, pas en anglais. |
| **Logiciels** | Firefox et LibreOffice en occitan, dictionnaire occitan pour LibreOffice. |
| **Clavier** | AZERTY occitan (`fr(oci)`) : les lettres occitanes en accès direct. |
| **Mises à jour** | Correctifs de sécurité Ubuntu et Mint installés automatiquement. |

Tout se règle dans un seul fichier, `/etc/occitux/occitux.conf` : interface en français, clavier français habituel, mises à jour manuelles.

## Ce qu'Occitux ne fait pas

- **Il ne remplace pas PrimTux.** Les logiciels éducatifs, les sessions par âge et le contrôle parental sont ceux de PrimTux, maintenus par son équipe.
- **Le menu de PrimTux reste en français** : il n'est pas encore traduisible. Voir la [feuille de route](docs/feuille-de-route.md).
- **Les traductions occitanes ne sont pas en gascon** : le système ne connaît qu'un seul occitan. Voir [la question de la langue](docs/lenga.md).

## Installer

**Sur un PC qui a déjà PrimTux 9** : télécharger `occitux_x.y.z_all.deb` depuis les [versions publiées](https://github.com/GMS64260/occitux/releases), puis :

```sh
sudo apt install ./occitux_*_all.deb
```

Redémarrer le PC. C'est tout.

**Sur plusieurs PC** : suivre le [guide des bénévoles](docs/guide-benevoles.md). On prépare un PC modèle, puis l'[outil de déploiement de PrimTux](https://framagit.org/primtux/outil-de-deploiement-primtux) le copie sur les autres en quelques minutes chacun.

## Changer un réglage

```sh
sudo nano /etc/occitux/occitux.conf   # LANGUE, CLAVIER, MISES_A_JOUR_AUTO
sudo occitux-config
```

Puis redémarrer le PC.

## Construire

Le paquet (Debian ou Ubuntu, `dpkg-deb` suffit) :

```sh
make paquet          # → construction/occitux_x.y.z_all.deb
make verifier        # shellcheck sur les scripts
```

L'ISO Occitux, à partir de l'ISO officielle de PrimTux (outils : `xorriso`, `squashfs-tools`) :

```sh
make iso ISO=~/Téléchargements/PrimTux9-M22.3-64bit-2026-02-27.iso
```

Le script vérifie que l'ISO est une version connue de PrimTux (`construire/sources-primtux.txt`), installe le paquet dans son système, puis réécrit l'ISO en gardant le démarrage de PrimTux intact.

## Organisation du dépôt

```
paquet/            le paquet occitux, tel qu'il sera installé
  DEBIAN/          description et scripts d'installation
  etc/occitux/     le fichier de réglages
  usr/sbin/        occitux-config, qui applique les réglages
construire/        fabrication de l'ISO à partir de celle de PrimTux
docs/              guide des bénévoles, langue, feuille de route
```

## Merci

- L'équipe [PrimTux](https://primtux.fr), qui fait tout le travail de fond.
- [Tot en òc](http://www.totenoc.eu) et Quentin Pagès, pour les traductions occitanes des logiciels libres.
- [Lo Congrès permanent de la lenga occitana](https://locongres.org), pour les outils de la langue.
- [mathieumd/Calandreta](https://github.com/mathieumd/Calandreta), le premier essai d'installation automatique pour une Calandreta (2014), qui a inspiré ce projet.

## Licence

GPL-3.0 ou ultérieure, comme PrimTux. Voir [LICENSE](LICENSE).
