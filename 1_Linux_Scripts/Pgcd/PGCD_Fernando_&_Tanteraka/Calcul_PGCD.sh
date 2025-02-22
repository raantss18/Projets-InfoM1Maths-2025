#!/bin/bash

# Fonction pour calculer le PGCD et les coefficients u, v par l'algorithme d'Euclide étendu
function pgcd_etendu {
    local a=$1
    local b=$2

    if [ "$b" -eq 0 ]; then
        echo "$a 1 0"
        return
    fi

    # Appel récursif
    read pgcd u v <<< $(pgcd_etendu $b $((a % b)))

    # Calcul des nouveaux coefficients
    local new_u=$((v))
    local new_v=$((u - (a / b) * v))

    echo "$pgcd $new_u $new_v"
}

# Demande à l'utilisateur de saisir deux nombres
echo "Entrez le premier nombre :"
read num1

echo "Entrez le deuxième nombre :"
read num2

# Vérification que les entrées sont des nombres positifs
if ! [[ "$num1" =~ ^[0-9]+$ && "$num2" =~ ^[0-9]+$ ]]; then
    echo "Veuillez entrer des nombres entiers positifs."
    exit 1
fi

# Capturer le temps de début
start_time=$(date +%s%N)  # Temps en nanosecondes

# Appel de la fonction avec les deux nombres
read pgcd u v <<< $(pgcd_etendu $num1 $num2)

# Capturer le temps de fin
end_time=$(date +%s%N)  # Temps en nanosecondes

# Calcul du temps écoulé en secondes
execution_time=$(( (end_time - start_time) / 1000000 ))  # Converti en millisecondes

# Affichage des résultats
echo "Le PGCD de $num1 et $num2 est : $pgcd"
echo "Les coefficients u et v sont : u = $u, v = $v"
echo "Vérification : $num1 * $u + $num2 * $v = $pgcd"
echo "Temps d'exécution : $execution_time ms"