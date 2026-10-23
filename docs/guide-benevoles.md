# Installer Occitux sur les PC de l'école

Ce guide s'adresse à un parent bénévole, pas forcément informaticien. Compter une demi-journée pour une salle de quelques PC.

## Ce qu'il faut

- Les PC : 64 bits, de 2010 ou plus récents, 2 Go de mémoire au minimum (4 Go c'est mieux), un disque d'au moins 40 Go.
- Une clé USB de 32 Go ou plus, **vide** : elle sera effacée.
- Un PC sous Linux pour préparer la clé (celui d'un parent suffit).

## Deux façons de faire

**La plus simple : la clé qui installe toute seule.** Quelqu'un prépare une clé avec l'ISO de déploiement d'Occitux (`occitux-x.y.z-deploiement.iso`, voir le README). Sur chaque PC : brancher la clé, allumer, attendre. Au bout de 20 secondes, Occitux s'installe sans poser de question, puis le PC demande de retirer la clé et s'éteint. On rallume : c'est fini, le PC est en occitan. Compter 10 à 20 minutes par PC, et plusieurs PC à la fois si on a plusieurs clés.

**Attention** : cette clé **efface tout le disque** de n'importe quel PC qui démarre dessus. Ne jamais la laisser traîner, ni la brancher sur le PC d'un parent. Si un PC démarre dessus par erreur, l'éteindre dans les 20 secondes.

Chaque PC installé de cette façon reçoit un nom `occitux-xxxx` différent, en occitan, avec les mises à jour automatiques. Il ne reste qu'à ajouter ce qui est propre à l'école (favoris, logiciels en plus), PC par PC, ou à passer par la seconde méthode.

**La seconde : le PC modèle.** On installe Occitux sur **un seul PC**, le modèle, on le règle aux petits oignons, on en fait une copie sur la clé USB, puis on recopie ce modèle sur les autres PC. C'est l'[outil de déploiement de PrimTux](https://framagit.org/primtux/outil-de-deploiement-primtux) qui fait les copies. Les étapes 2 à 6 ci-dessous décrivent cette méthode. L'étape 1 vaut pour les deux.

## 1. Préparer chaque PC (5 minutes par PC)

Au démarrage, entrer dans le BIOS (souvent touche `F2`, `F10`, `Suppr` ou `Échap`, selon la marque) et :

- **désactiver le Secure Boot** : PrimTux ne démarre pas sans ça ;
- mettre la clé USB en premier dans l'ordre de démarrage.

### Vérifier la mémoire des PC reconditionnés

Sur un PC d'occasion, la mémoire vive est souvent la pièce qui pose problème : barrette fatiguée, ou barrettes ajoutées qui ne vont pas ensemble. Le PC peut sembler marcher sous Windows et planter avec Occitux.

**Le symptôme** : le PC plante en quelques secondes, avant tout affichage d'Occitux, avec un message qui finit par

```
Kernel panic - not syncing: Attempted to kill init! exitcode=0x00000009
```

et, plus haut, des mots comme `kmalloc`. Ce message ne dit pas « mémoire », mais c'est presque toujours elle.

**Que faire** :

1. Au menu de démarrage de la clé, choisir **« Tester la mémoire »**. Le test tourne tout seul ; au bout d'un passage complet (une demi-heure environ), la case `Errors` doit rester à `0`. Une seule erreur suffit à condamner une barrette.
2. S'il y a plusieurs barrettes, essayer **une seule barrette à la fois**, dans le premier emplacement, pour trouver la mauvaise.
3. Sur les PC d'avant 2012 environ, **ne pas mélanger de la DDR3L (basse tension, 1,35 V) avec de la DDR3 (1,5 V)** : ces PC n'acceptent que la DDR3 à 1,5 V. L'étiquette de la barrette indique `PC3L` pour la DDR3L et `PC3` pour la DDR3.
4. Mieux vaut **une seule bonne barrette de 4 Go** que 6 Go faits de barrettes dépareillées : Occitux tourne avec 2 Go, 4 Go est confortable.

## 2. Préparer la clé USB (une seule fois)

Suivre les étapes 1 et 2 de la [notice de l'outil de déploiement](https://framagit.org/primtux/outil-de-deploiement-primtux) : un script crée la clé, puis on y copie le fichier `deploiement-primtux.iso`.

Copier aussi sur la clé, dans le dossier `ventoy`, l'ISO Occitux (`occitux-x.y.z.iso`).

## 3. Installer le PC modèle

1. Démarrer le PC sur la clé et choisir l'ISO Occitux.
2. Choisir « Installer Occitux automatiquement » (tout le disque est effacé) ou « Installer Occitux » pour choisir soi-même le disque. Prendre **le plus petit disque** de tous les PC : on ne pourra pas copier le modèle sur un disque plus petit que le sien.
3. Redémarrer. Le PC s'ouvre en occitan.
4. Ajouter ce qui est propre à l'école : logiciels en plus, favoris, réglages des sessions.

**Pour mettre l'interface en français** au lieu de l'occitan : ouvrir un terminal et taper

```sh
sudo nano /etc/occitux/occitux.conf
```

remplacer `LANGUE=oc` par `LANGUE=fr`, enregistrer (`Ctrl+O`, `Entrée`, `Ctrl+X`), puis taper `sudo occitux-config` et redémarrer.

## 4. Copier le modèle sur la clé

Démarrer le PC modèle sur la clé, choisir `deploiement-primtux`, puis cliquer sur **Réaliser une image de PrimTux**. Lui donner un nom, par exemple `occitux-ecole`.

## 5. Copier le modèle sur chaque PC (5 à 15 minutes par PC)

Sur chaque PC : démarrer sur la clé, choisir `deploiement-primtux`, puis **Déployer PrimTux sur le disque principal**. Avec plusieurs clés, on fait plusieurs PC en même temps.

## 6. Donner un nom à chaque PC

Après la copie, tous les PC portent le même nom. Pour les distinguer sur le réseau, lancer sur chacun le script `chnompc.sh` de l'outil de déploiement :

```sh
sudo ./chnompc.sh calandreta-pc1
```

## En cas de problème

- **Le PC ne démarre pas sur la clé** : le Secure Boot est encore actif, ou la clé n'est pas en premier dans l'ordre de démarrage.
- **`Kernel panic` dès le démarrage** : voir « Vérifier la mémoire des PC reconditionnés » plus haut.
- **La clé se comporte bizarrement** (plantages différents à chaque essai, clé invisible) : les clés sans marque sont souvent en cause. Prendre une clé de marque.
- **La copie refuse de se faire** : le disque du PC est plus petit que celui du modèle.
- **Une question sur PrimTux** : le [forum PrimTux](https://forum.primtux.fr) est très actif.
- **Une question sur Occitux** : ouvrir un ticket sur [GitHub](https://github.com/GMS64260/occitux/issues).
