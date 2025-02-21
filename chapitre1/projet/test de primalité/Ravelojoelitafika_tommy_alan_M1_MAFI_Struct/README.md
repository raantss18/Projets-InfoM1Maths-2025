# primality-test
test de primalité utilisant un algorithme simple.	

Cet algorithme utilise le principe de la division successive avec quelques modifications pour optimiser la vitesse de calcul du test.

## A-Algorithme pour la verification de la valeur entrée

-**Lecture de la valeur entrée**  
Capture de la valeur à tester

-**Vérification de la valeur entrée**  
Validation que la valeur est bien un entier relatif

-**Utilisation de la valeur absolue**  
Pour éviter les problèmes de congruence en bash, nous utilisons la valeur absolue du nombre entré

## B-ALgorithme pour améliorer la vitesse de calcul 

- **Vérification de la parité**    
pour réduire le nombre de tests de divisibilité de moitié	 
- **Calcul de la racine carrée pour**  
limiter les tests

## Nécessitée de la racine carrée

Le calcul de la racine carrée permet de réduire significativement le nombre de tests de divisibilité nécessaires. Voici pourquoi :

Si on pose :
- r = la racine carrée d'un nombre n (r × r = n)
- p et q deux facteurs tels que p × q = n

On a forcément p ≤ r ou q ≤ r, car si p > r et q > r, alors :
p × q > r × r = n, ce qui est impossible.

Donc, pour vérifier la non-primalité de n, il suffit de trouver un facteur inférieur ou égal à r qui divise n.

## C-Algoithme pour les nombres non carrée parfaits
- **Test de la divisibilité par les nombres impairs inférieurs à la racine carrée**

## Retour de primalité

