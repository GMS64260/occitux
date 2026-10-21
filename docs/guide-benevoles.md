# Installer Occitux sur les PC de l'école

Ce guide s'adresse à un parent bénévole, pas forcément informaticien. Compter une demi-journée pour une salle de quelques PC.

## Ce qu'il faut

- Les PC : 64 bits, de 2010 ou plus récents, 2 Go de mémoire au minimum (4 Go c'est mieux), un disque d'au moins 40 Go.
- Une clé USB de 32 Go ou plus, **vide** : elle sera effacée.
- Un PC sous Linux pour préparer la clé (celui d'un parent suffit).

## Le principe

On installe Occitux sur **un seul PC**, le modèle. On en fait une copie sur la clé USB. Puis on recopie ce modèle sur les autres PC, en quelques minutes chacun. C'est l'[outil de déploiement de PrimTux](https://framagit.org/primtux/outil-de-deploiement-primtux) qui fait les copies.

## 1. Préparer chaque PC (5 minutes par PC)

Au démarrage, entrer dans le BIOS (souvent touche `F2`, `F10`, `Suppr` ou `Échap`, selon la marque) et :

- **désactiver le Secure Boot** : PrimTux ne démarre pas sans ça ;
- mettre la clé USB en premier dans l'ordre de démarrage.

## 2. Préparer la clé USB (une seule fois)

Suivre les étapes 1 et 2 de la [notice de l'outil de déploiement](https://framagit.org/primtux/outil-de-deploiement-primtux) : un script crée la clé, puis on y copie le fichier `deploiement-primtux.iso`.

Copier aussi sur la clé, dans le dossier `ventoy`, l'ISO Occitux (`occitux-x.y.z.iso`).

## 3. Installer le PC modèle

1. Démarrer le PC sur la clé et choisir l'ISO Occitux.
2. Lancer l'installation et suivre les écrans. Prendre **le plus petit disque** de tous les PC : on ne pourra pas copier le modèle sur un disque plus petit que le sien.
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
- **La copie refuse de se faire** : le disque du PC est plus petit que celui du modèle.
- **Une question sur PrimTux** : le [forum PrimTux](https://forum.primtux.fr) est très actif.
- **Une question sur Occitux** : ouvrir un ticket sur [GitHub](https://github.com/GMS64260/occitux/issues).
