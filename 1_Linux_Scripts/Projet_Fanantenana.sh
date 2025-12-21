#!/bin/bash

# Fonction pour calculer le PGCD
pgcd() {
    a=$1
    b=$2
    
    while [ $b -ne 0 ]; do
        reste=$((a % b))
        a=$b
        b=$reste
    done
    
    echo $a
}

# Vérification du nombre d'arguments
if [ $# -ne 2 ]; then
    echo "Usage: $0 nombre1 nombre2"
    exit 1
fi

# Vérification que les arguments sont des nombres entiers
if ! [[ $1 =~ ^[0-9]+$ ]] || ! [[ $2 =~ ^[0-9]+$ ]]; then
    echo "Erreur: Les deux arguments doivent être des nombres entiers positifs"
    exit 1
fi

# Appel de la fonction pgcd et affichage du résultat
resultat=$(pgcd $1 $2)
echo "PGCD de $1 et $2 est: $resultat"