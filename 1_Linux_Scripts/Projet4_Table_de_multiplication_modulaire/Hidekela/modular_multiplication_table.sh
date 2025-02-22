#!/bin/bash

# Le code marche bien mais le temps d'execution ne s'affiche pas
echo ""
echo "---------------------------------"
echo "Table de Multiplication Modulaire"
echo "---------------------------------"
echo ""

read -p "Entrer un nombre entier n: " n
read -p "Entrer le nombre module m: " m

echo ""
echo "Voici la table de multiplication $n mod $m:"
echo ""

for (( i=1; i<=10; i++))
do
	echo "($n x $i) mod $m = $(( (n*i)%m ))"
done
