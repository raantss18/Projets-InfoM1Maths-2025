#!/bin/bash

# Fonction pour demander et lire le nombre
echo "Entrez un nombre entier : "
read nombre

# Vérification que le nombre est entier
nombre_original=$nombre
nombre_entier=$(echo "scale=0; $nombre" | bc)
difference=$(echo "$nombre_original - $nombre_entier" | bc)
if [ $(echo "$difference != 0" | bc) -eq 1 ]; then
    echo "Erreur : Veuillez entrer un nombre entier"
    exit 1
fi

# Test si le nombre est négatif et utilisation de sa valeur absolu si nécessaire
if [ $nombre -lt 0 ]; then
    nombre=$((nombre * -1))
fi

# Test de divisibilité par 2
if [ $((nombre % 2)) -eq 0 ] && [ $nombre -ne 2 ]; then
    echo "$nombre n'est pas premier (divisible par 2)"
    exit 0
fi

test_premier=1

# Calcul de la partie entière de la racine carrée
Partie_Ent_racine=$(echo "scale=0; sqrt($nombre)" | bc)

# Vérifie si la racine carrée est entière
if [ $((Partie_Ent_racine * Partie_Ent_racine)) -eq $nombre ]; then
    echo "$nombre n'est pas premier (c'est un carré parfait)"
    exit 0
fi

# Test de congruence modulo 2n+1
limite=$(( (Partie_Ent_racine - 1) / 2 ))

for ((n=1; n <= limite; n++)); do
    diviseur=$((2 * n + 1))
    if [ $((nombre % diviseur)) -eq 0 ]; then
        echo "$nombre n'est pas premier (divisible par $diviseur)"
        test_premier=0
        break
    fi
done

# Affichage du résultat final
if [ $test_premier -eq 1 ]; then
    echo "$nombre est premier"
fi
