# Interpolation de Lagrange

Ce projet implémente l'interpolation de Lagrange en Python pour approcher une fonction à partir d'un ensemble de points donnés. Le programme prend des points \((x_i, y_i)\) en entrée via la console, calcule le polynôme interpolateur, l'évalue pour des points spécifiques, et affiche une visualisation graphique.

## Objectif
- Construire un polynôme \(L(x)\) qui passe exactement par un ensemble de points \((x_i, y_i)\), \(i=0,\dots,n\).
- Implémenter la formule de Lagrange :  
  \[
  L(x) = \sum_{i=0}^n y_i \prod_{j \neq i} \frac{x - x_j}{x_i - x_j}
  \]
- Évaluer \(L(x)\) pour des valeurs arbitraires et tracer le polynôme.

## Prérequis
- Python 3.x
- Bibliothèques Python :
  - `numpy`
  - `matplotlib`

### Installation
1. Clonez ou téléchargez ce dépôt.
2. Installez les dépendances avec pip :
   ```bash
   pip install numpy matplotlib