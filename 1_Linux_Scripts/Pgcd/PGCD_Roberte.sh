#!/bin/bash
 
# Demande des deux nombres
read -p "entrer le premier nombre: " a
read -p "entrer le second nombre: " b
# Fonction pour calculer le pgcd des deux nombres en utilisant l'algorithme d'Euclide
pgcd() {
        local a=$a
        local b=$b
        while [ $b -ne 0 ]; do
            local t=$b
            b=$((a % b))
            a=$t
        done 
        echo $a
}
# Calcul du temps d'execution
start_time=$(date +%s%N)
result=$(pgcd $a $b)
end_time=$(date +%s%N)
# Calcul du temps écoulé en nanosecondes
elapsed_time=$((end_time - start_time))
# Affichage des résultats                       
echo "le PGCD de $b et $a  est: $result"
echo "le temps d'exécution: $elapsed_time nanosecondes" 
