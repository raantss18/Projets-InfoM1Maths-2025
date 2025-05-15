# Approximation de π par la méthode de Monte Carlo

![Visualisation Monte Carlo](https://via.placeholder.com/800x400?text=Monte+Carlo+Pi+Visualization)

Ce projet implémente une simulation Monte Carlo pour estimer la valeur de π en Python, avec visualisation en temps réel des points aléatoires et de la convergence de l'estimation.

## Principe mathématique

La méthode consiste à :
1. Générer des points aléatoires dans un carré de côté 2 (coordonnées de -1 à 1)
2. Compter les points qui tombent dans le cercle unité inscrit (distance ≤ 1 depuis l'origine)
3. Le rapport (points dans le cercle)/(points totaux) ≈ π/4

## Fonctionnalités

- Génération de points aléatoires avec visualisation immédiate
- Deux modes d'affichage :
  - Mode accumulatif (tous les points)
  - Mode dynamique (seuls les derniers points)
- Graphique de convergence montrant l'évolution de l'estimation
- Calcul automatique de l'erreur relative

## Prérequis

- Python 3.6+
- Bibliothèques requises :
  ```bash
  numpy
  matplotlib