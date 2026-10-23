# Feuille de route

## 0.1 : la couche occitane (en cours)

- [x] Paquet `occitux` : langue occitane avec repli en français, clavier occitan, Firefox et LibreOffice en occitan, mises à jour de sécurité automatiques
- [x] Réglages dans un seul fichier, `occitux-config` pour les appliquer
- [x] Script de construction de l'ISO à partir de l'ISO officielle de PrimTux 9
- [x] Test automatique du paquet sur Ubuntu 24.04
- [x] Construire l'ISO à partir de PrimTux 9 et la démarrer en machine virtuelle (UEFI, session live) : la session élève s'ouvre, la date s'affiche en occitan
- [x] Les sessions élèves de PrimTux (Jerry, Koda, Léon, Poe) n'imposent ni langue ni clavier : elles suivent ceux du système
- [x] Démarrage en BIOS ancien (Legacy) en machine virtuelle : menu Occitux, puis écran des élèves
- [ ] Installation sur disque, puis vérification du service de premier démarrage
- [ ] Vérifier la frappe au clavier occitan dans une session élève
- [ ] Installer sur un vrai PC reconditionné

- [x] GCompris reste en français au lieu de basculer en anglais (il n'a pas de traduction occitane)
- [x] Firefox : les sites sans occitan s'affichent en français, pas en anglais
- [x] Menus de démarrage « Essayer Occitux » et « Installer Occitux »
- [x] Option `LANGUE=bearnes` : béarnais, puis occitan, puis français
- [x] Entrée « Tester la mémoire » (memtest86+, BIOS et UEFI) et section mémoire du guide des bénévoles, après un Acer Aspire 4820TG qui plantait au démarrage à cause d'une barrette
- [x] Premiers catalogues béarnais (`traductions/gascon/`) : bureau XFCE, Thunar, Tux Paint, écran de connexion (fusionnés le 2026-10-23)

## 0.2 : Occitux à la place de PrimTux, installation sans un clic (en cours)

- [x] Installation automatique : preseed Ubiquity, choix du plus grand disque interne, extinction en fin d'installation, nom de PC `occitux-xxxx`
- [x] ISO de déploiement (`OCCITUX_INSTALLATION=automatique`) : l'installation démarre seule après 20 secondes
- [x] Le PC se présente comme Occitux : `os-release`, GRUB, écran de connexion, fonds d'écran des quatre sessions (logo Occitux à la place de celui de PrimTux), menus de démarrage, nom de volume de l'ISO
- [x] Menu des élèves en occitan et en béarnais : gabarits, scripts, catégories (fichiers détournés par `dpkg-divert`, refaits à chaque mise à jour du menu par un déclencheur dpkg)
- [x] Écran de connexion, diaporama d'installation et message de fin (« retirez la clé ») en occitan
- [ ] Vérifier l'installation automatique en machine virtuelle (UEFI et BIOS), puis sur un vrai PC
- [ ] Descriptions des logiciels du menu en occitan
- [ ] Panneau d'accueil de la session Poe (« Accueil ») en occitan
- [ ] Choix de la Calandreta à l'installation (nom des PC, logo)
- [ ] Guide des bénévoles relu par un bénévole qui n'est pas informaticien

## Plus tard : avec les autres projets

- [ ] Présenter Occitux à l'équipe PrimTux, qui a prévu l'internationalisation de son menu, et proposer la traduction occitane une fois le menu traduisible
- [ ] Demander à Lo Congrès une licence libre pour le correcteur gascon (voir [la question de la langue](lenga.md))
- [ ] Compléter la traduction occitane de XFCE et des logiciels éducatifs, avec Tot en òc
- [ ] Contenus occitans pour les élèves : comptines, dictionnaire, ressources pédagogiques
- [ ] Faire connaître Occitux aux autres Calandretas
