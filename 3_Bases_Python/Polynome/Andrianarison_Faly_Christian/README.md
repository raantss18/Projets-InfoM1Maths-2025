# PROJET 8: POLYNOMES
Nom et prénoms: Andrianarison Faly Christian  
Parcours: MAFI

## L’objectif du projet.
Créer une classe `Polynome` pour manipuler des polynômes.  
Manipuler : afficher le polynome, évaluer le pôlynome, additionner deux polynômes, multiplier deux polynômes, multipler un polynôme par un scalaire.

## Les étapes de la solution
- `def __init__(self, entries:list)`: prend en entrée les coefficients du polynômes sous forme d'une liste de nombres; supprime les zéros à la fin de la liste si il y en a; crée deux attributs `Polynome.entries` (les coefficients) et `Polynome.degree` (dégré).

- `def __str__(self) -> str`: AFFICHAGE  
Renvoi une chaîne de caractères qui représente le polynôme dans la base canonique

- `def of(self, x:float) -> float`: EVALUATION  
Evalue le polynôme en `x` an calculant chaque puissance de `x` et le multipliant par le coefficient correspondant. 

- `def __add__(self, OTHER:"Polynome") -> "Polynome"`: ADDITION  
Additionne deux polynômes: addition coefficient par coefficient

- `def __mul__(self, OTHER) -> "Polynome":`: MULTIPLICATION (polynome-polynome ou polynome-scalaire)  
Si `OTHER` est un polynôme, alors on multiplie chaque monôme de `self` par `OTHER` et on fait la somme de tous ces produits. Sinon si `OTHER` est un scalaire: on le transforme `OTHER` en type `Polynome` (constant) et on fait la multiplication commme précédement.

- `def __rmul__(self, x) -> "Polynome":`: MULTIPLICATION de type `scalaire * Polynome`  
Utilise la fonction précédente pour renvoyer le produit. 

- `def __sub__(self, OTHER:"Polynome") -> "Polynome"`: SOUSTRACTION  
Utilise les fonctions précedentes pour renvoyer : `self + (-1)*OTHER`

## Quelques tests et résultats
On a créé la fonction `test()` pour tester la classe.  
En éxécutant le script, on nous affiche:  
`*** POLYNOMES ***`  
P(x) = 1 + x   
 => P(1) = 2  
Q(x) = 2 - 3x - 8x^3 + 9x^4   
 => Q(-2) = 216  
N(x) = 0  
P(x) + Q(x) = 3 - 2x - 8x^3 + 9x^4  
P(x) * Q(x) = 2 - x - 3x^2 - 8x^3 + x^4 + 9x^5  
P(x) * N(x) = 0  
-2 * Q(x) = -4 + 6x + 16x^3 - 18x^4  

## Les limites éventuelles:
`P = Polynome(range(N+1))`: crée un polynome de dégré N. Puis j'ai calculé: `P*P`: 
- pour N = 1000: il a pris moins de 1s pour faire le calcul;
- pour N = 10000: ça a pris environ 25s 