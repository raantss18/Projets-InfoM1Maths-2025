#!/bin/bash

# Fonction pour calculer le PGCD en utilisant l'algorithme d'Euclide
pgcd() {
    local a=$1
    local b=$2
    while [ $b -ne 0 ]; do
        local temp=$b
        b=$((a % b))
        a=$temp
    done
    echo $a
}

# Demander deux nombres à l'utilisateur
read -p "Entrez le premier nombre : " nb1
read -p "Entrez le deuxième nombre : " nb2

# Mesurer le temps d'exécution
start_time=$(date +%s%N)  # Temps de début en nanosecondes

# Calculer le PGCD
result=$(pgcd $nb1 $nb2)

end_time=$(date +%s%N)  # Temps de fin en nanosecondes

# 1 nanoseconde vaut 10^-9 secondes tandis que 1 milliseconde vaut 10^-3 secondes d'où 1 nanoseconde vaut 10^-6 millisecondes

# Calculer la durée d'exécution en nanosecondes et la convertir en millisecondes
duration=$(( (end_time - start_time) / 1000000 ))

# Afficher le résultat et le temps d'exécution
echo "Le PGCD de $num1 et $num2 est : $result"
echo "Temps d'exécution : $duration millisecondes"
