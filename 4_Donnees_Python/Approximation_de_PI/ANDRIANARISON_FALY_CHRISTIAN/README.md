# PROJET 4: APPROXIMATION DE PI PAR LA MÉTHODE MONTE CARLO
Nom et prénoms: ANDRIANARISON Faly Christian   
Parcours: MAFI  

## L’objectif du projet.
Utiliser la méthode de Monte Carlo pour approximer la valeur de π.  
Visualiser l'erreur d'approximation en fonction du nombre d'itérations.

## Les étapes de la solution
- `def MonteCarlo(prec:int) -> tuple`: Approximation de π  
  Utilise la méthode de Monte Carlo pour approximer π avec une précision donnée. La fonction continue à générer des points aléatoires jusqu'à ce que l'erreur soit inférieure à 10^(-prec).

- `def show_error(N:int)`: Visualisation de l'erreur  
  Génère un graphique montrant l'évolution de l'erreur d'approximation de π en fonction du nombre d'itérations.

## Quelques tests et résultats
En exécutant le script via `python3 monteCarlo.py` , l'utilisateur est invité à entrer le nombre d'itérations pour l'approximation. Le programme affiche ensuite l'approximation de π avec l'erreur correspondante et trace la courbe de l'erreur en fonction du nombre d'itérations avec `matplotlib`.