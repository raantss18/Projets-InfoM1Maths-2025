

```markdown
nom et prenoms:RANDRIANJAFY Voahanginiaina Roberte
# Etude de la Suite de Fibonacci

## Description

Ce projet implémente la suite de Fibonacci à l'aide d'une fonction récursive en Python. Le programme calcule les 20 premiers termes de la suite et les affiche dans le terminal. De plus, il génère des graphiques qui visualise les termes de la suite et qui analyse son comportement asymptotique. La suite de Fibonacci est une suite mathématique définie par :

\[
F(0) = 0, \quad F(1) = 1, \quad F(n) = F(n-1) + F(n-2) \text{ pour } n > 1
\]

## Fonctionnalités

- Calcul des 20 premiers termes de la suite de Fibonacci de manière récursive.
- Affichage des termes de la suite dans le terminal.
- Visualisation graphique des termes de la suite de Fibonacci.
- Comparaison graphique entre la suite de Fibonacci et son comportement asymptotique (croissance exponentielle).
- Analyse de la croissance asymptotique de la suite de Fibonacci, qui suit une croissance proche de \( \frac{\phi^n}{\sqrt{5}} \), où \( \phi \) est le nombre d'or(environ 1,608).

## Prérequis

Avant d'exécuter le programme, vous devez avoir installé Python et les bibliothèques suivantes :

- Python 3.x
- `matplotlib` pour la visualisation graphique.

Vous pouvez installer `matplotlib` via `pip` :

```bash
pip install matplotlib
```

## Instructions d'utilisation

1. **Cloner le projet :**

   Clonez ce repository sur votre machine locale en utilisant Git :

   ```bash
   git clone https://github.com/votre-nom-utilisateur/nom-du-repository.git
   ```

2. **Exécuter le programme :**

   Une fois le projet cloné, vous pouvez exécuter le programme Python à l'aide de la commande suivante :

   ```bash
   python fibonacci_suite_recursive.py
   ```

   Ce programme calculera et affichera les 20 premiers termes de la suite de Fibonacci dans le terminal. Il génèrera également deux graphiques :
   - Le premier montre les termes de la suite de Fibonacci.
   - Le second compare la suite avec sa croissance asymptotique (approximée par \( \frac{\phi^n}{\sqrt{5}} \)).

## Explication du comportement asymptotique

La suite de Fibonacci suit une croissance exponentielle à long terme. Plus précisément, elle croît comme une puissance du nombre d'or \( \phi \)(environ 1,618), où :

\[
F(n) \sim \frac{\phi^n}{\sqrt{5}}
\]

Cela signifie que plus \( n \) devient grand, plus la suite de Fibonacci se rapproche de cette expression asymptotique. Dans le programme, nous avons tracé cette approximation pour observer la convergence de la suite réelle vers la courbe asymptotique.

## Structure du code

Le programme est divisé en deux parties principales :
- **La fonction récursive** `fibonacci(n)`, qui calcule le terme \( n \)-ième de la suite de Fibonacci.
- **La partie graphique**, qui génère des visualisations de la suite et de son comportement asymptotique à l'aide de la bibliothèque `matplotlib`.

## Exemple de sortie

Lorsque vous exécutez le programme, vous devriez voir une sortie similaire à ceci dans votre terminal :

```
Les 20 premiers termes de la suite de Fibonacci:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
```

En plus de cela, vous verrez deux graphiques générés par `matplotlib` :
- Le premier graphique montre l'évolution des termes de la suite de Fibonacci dont la courbe est bleu.
- Le deuxième graphique compare la suite de Fibonacci avec son comportement asymptotique .

