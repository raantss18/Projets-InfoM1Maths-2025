#!/bin/bash

# le code s'execute avec des erreurs et ne donne pas le résultat voulu. A revoir

# le code présenter des erreurs à cause des commandes bc

#arpes quelques recherches j'ai pu trouver des alternatives à cette commande tout en conservant la structure de l'algorithme 

#ce nouveau code devrait se lancer sans erreurs 

# Fonction pour vérifier si un nombre est entier
verifier_entier() {
    if [[ ! $1 =~ ^-?[0-9]+$ ]]; then
        echo "Erreur : Veuillez entrer un nombre entier"
        exit 1
    fi
}

# Fonction pour calculer la racine carrée entière
calculer_racine() {
    local n=$1
    local i=1
    while ((i * i <= n)); do
        ((i++))
    done
    echo $((i - 1))
}

# Demander et lire le nombre
echo "Entrez un nombre entier : "
read nombre

# Vérification que le nombre est entier
verifier_entier "$nombre"

# Test si le nombre est négatif et utilisation de sa valeur absolue si nécessaire
if [ $nombre -lt 0 ]; then
    nombre=$((nombre * -1))
fi

# Test des cas spéciaux (0 et 1)
if [ $nombre -eq 0 ] || [ $nombre -eq 1 ]; then
    echo "$nombre n'est pas premier"
    exit 0
fi

# Test si le nombre est 2 (seul nombre premier pair)
if [ $nombre -eq 2 ]; then
    echo "$nombre est premier"
    exit 0
fi

# Test de divisibilité par 2
if [ $((nombre % 2)) -eq 0 ]; then
    echo "$nombre n'est pas premier (divisible par 2)"
    exit 0
fi

# Calcul de la racine carrée entière
racine=$(calculer_racine $nombre)

# Test si c'est un carré parfait
if [ $((racine * racine)) -eq $nombre ]; then
    echo "$nombre n'est pas premier (c'est un carré parfait)"
    exit 0
fi

test_premier=1

# Test de divisibilité par les nombres impairs
limite=$(( (racine - 1) / 2 ))

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
    echo "$nombre es
    t premier"
fi
