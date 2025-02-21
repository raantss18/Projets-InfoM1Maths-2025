# FACTORISATION D'UN ENTIER

Le script `bash` `factorisation_projet3.sh` contient :
1. deux (2) fonctions:
- `factorisation_naive()`: elle prend un entier `n` en entrée, essaie de diviser `n` par les entiers inférieurs (ou égal) à `sqrt(n)`  et affiche `n` sous la forme `pq` où `p` est le premier diviseur non trivial de `n` trouvé. Si aucun diviseur non trivial n'est trouvé, on affiche `n est un nombre premier`.

- `produit_de_premier()`: cette fonction prend un entier `n` entrée et renvoie la decomposition de `n` sous la forme `n = 1 * p1^e1 * p2^e2 * ...` où `p1, p2,...` sont des nombres premiers.
L'algorithme de décomposition se résume comme suit: on génère un nombre premier `p` (en commençant par 2); puis on teste si `p` disive `n`; si c'est le cas, on divide `n` par `p` successivement pour savoir l'exposant `e` associé à `p` et on assigne la valeur `n / p^e` à `n`. Ensuite, on génère le nombre premier suivant et on refait le même test avec la nouvelle valeur de `n` et de `p`. L'algorithme s'arrête quand `n` vaut `1`.

2. un script qui demande à l'utilisateur d'entrer un nombre entier supérieur à 2 à factoriser; puis teste si la valeur entrée est bien un entier supérieur à 2; si c'est le cas, on le factorise à l'aide de l'une des fonctions mentionées précédement et affiche le resultat; sinon on redemande d'entrer un entier supérieur à 2. Le programme affiche le temps d'execution du programme (en seconde).



