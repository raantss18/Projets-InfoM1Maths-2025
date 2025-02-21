#!/bin/bash

#A revoir car cela ne marche pas

# Fonction pour calculer le PGCD en utilisant l>
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

# Demander à l'utilisateur de saisir deux nombr>
read -p "Entrez le premier nombre: " num1
read -p "Entrez le deuxième nombre: " num2

# Enregistrer le temps de début
start_time=$(date +%s%N)
# Calculer le PGCD
result=$(pgcd $num1 $num2)

# Enregistrer le temps de fin
end_time=$(date +%s%N)

# Calculer le temps d'exécution en millisecondes
execution_time=$(( (end_time - start_time) / 10>

# Afficher le résultat
echo "Le PGCD de $num1 et $num2 est: $result"
echo "Temps d'exécution: $execution_time millis>
