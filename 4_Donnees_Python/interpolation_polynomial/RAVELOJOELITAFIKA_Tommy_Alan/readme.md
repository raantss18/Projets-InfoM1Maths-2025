# Interpolation par Polynôme via Matrice de Vandermonde

Ce script Python permet de réaliser une interpolation par polynôme à partir d'un ensemble de points définis dans un fichier CSV. La méthode utilisée repose sur la construction d'une matrice de Vandermonde et la résolution du système linéaire associé par l'élimination de Gauss.

## Prérequis

- **Python 3.x**
- **Bibliothèques Python** :  
  - `matplotlib` (pour le tracé des courbes)  
  - `csv` (pour la lecture du fichier CSV)
- **Fichier CSV** : Un fichier nommé `points.csv` contenant les points à interpoler.  
  **Important** : Les valeurs de `x` doivent être toutes différentes pour assurer une bonne interpolation.

## Fonctionnement du Code

### 1. Lecture des Points depuis le CSV
- Le script ouvre le fichier `points.csv` en mode lecture.
- Il ignore la première ligne (entête) et lit les lignes suivantes.
- Les valeurs sont converties en nombres flottants et stockées dans deux listes : `x_points` et `y_points`.

### 2. Construction de la Matrice de Vandermonde
- Pour chaque point `x` lu, une ligne est créée sous la forme `[1, x, x², ..., x^(n-1)]`, où `n` est le nombre total de points.
- Cette matrice permet de formuler le système d'équations linéaires dont les inconnues sont les coefficients du polynôme.

### 3. Résolution du Système par Élimination de Gauss
- Le système linéaire obtenu (Matrice de Vandermonde × Coefficients = `y_points`) est résolu par l'algorithme d'élimination de Gauss.
- L'objectif est de transformer la matrice en une forme triangulaire supérieure.
- Pendant ce processus, les valeurs de `y_points` sont également modifiées afin de faciliter la résolution par substitution arrière.

### 4. Calcul des Coefficients du Polynôme
- Après avoir obtenu une matrice triangulaire, une substitution arrière est effectuée.
- Cela permet de déterminer successivement les coefficients du polynôme d'interpolation.
- Le polynôme est alors défini par la somme des termes `coefficients[i] * x^i`.

### 5. Affichage du Polynôme et Tracé de la Courbe
- L'expression du polynôme d'interpolation est affichée dans la console.
- Une suite dense de points est générée sur l'axe des `x` afin d'évaluer et tracer la courbe du polynôme.
- Les points d'interpolation sont affichés en rouge tandis que la courbe est tracée en bleu, facilitant ainsi la visualisation.

## Méthode d'Interpolation (Matrice de Vandermonde)

La méthode repose sur les étapes suivantes :

1. **Construction de la Matrice**  
   Pour un ensemble de points \((x_i, y_i)\), la matrice de Vandermonde \(V\) est construite de sorte que chaque ligne soit :
   [1, x_i, x_i², ..., x_i^(n-1)]
Ce qui donne le système :
   V * a = y
où \(a\) est le vecteur des coefficients inconnus du polynôme.

2. **Élimination de Gauss**  
Le système est résolu en appliquant l'élimination de Gauss pour transformer la matrice \(V\) en une forme triangulaire supérieure. Cela simplifie le calcul des coefficients via une substitution arrière.

3. **Calcul des Coefficients**  
Une fois la matrice triangulaire obtenue, les coefficients du polynôme sont calculés par substitution arrière, permettant de reconstruire la fonction polynomiale d'interpolation.

**Remarque** : Pour que la méthode soit valide, il est impératif que toutes les valeurs de \(x\) soient différentes. Sinon, la matrice de Vandermonde devient singulière et le système ne peut pas être résolu correctement.

## Comment Utiliser le Code

1. **Préparer le Fichier CSV**  
Créez un fichier nommé `points.csv` dans le même répertoire que le script. Le fichier doit contenir :
- Une première ligne d'entête (qui sera ignorée).
- Des lignes avec deux valeurs séparées par le séparateur approprié représentant les coordonnées \(x\) et \(y\).

Exemple de contenu :
```csv
x,y
1,2
2,3
3,5
4,4
