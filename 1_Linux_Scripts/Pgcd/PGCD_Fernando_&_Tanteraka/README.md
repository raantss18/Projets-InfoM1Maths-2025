# Calcul du PGCD par l'Algorithme d'Euclide Étendu

## Description

Ce projet implémente un script Bash qui calcule le **Plus Grand Commun Diviseur (PGCD)** de deux nombres entiers positifs en utilisant **l'algorithme d'Euclide étendu**. En plus du PGCD, le script retourne également les coefficients $ u $ et $ v $ tels que :

$$
a \cdot u + b \cdot v = \text{PGCD}(a, b)
$$

Le script inclut également une mesure du temps d'exécution pour évaluer la performance.

---

## Auteurs

- **ZAMANILEHA Elorgin Fernando**
- **RANDRIANIRINA Setraniaina Fanilo Tanteraka**

---

## Prérequis

Pour exécuter ce script, vous devez avoir les éléments suivants installés sur votre système :

1. **Bash** : Le script est écrit en Bash et doit être exécuté dans un terminal Unix/Linux.
2. **GNU Core Utilities** : Les commandes comme `date` et `read` sont nécessaires pour mesurer le temps d'exécution.

Si vous utilisez un système Windows, assurez-vous d'utiliser **WSL (Windows Subsystem for Linux)** ou une distribution Linux.

---

## Instructions d'Utilisation

1. Téléchargez ou copiez le script `Calcule_PGCD.sh` sur votre machine.
2. Ouvrez un terminal et naviguez jusqu'au répertoire contenant le script.
3. Rendez le script exécutable avec la commande suivante :
   ```bash
   chmod +x Calcule_PGCD.sh
   ```

---

## Exemple d'Exécution

Voici un exemple concret d'utilisation du script :

```cmd
$ ./Calcule_PGCD.sh
Entrez le premier nombre :
35
Entrez le deuxième nombre :
15
Le PGCD de 35 et 15 est : 5
Les coefficients u et v sont : u = 1, v = -2
Vérification : 35 * 1 + 15 * -2 = 5
Temps d'exécution : 1 ms
```
