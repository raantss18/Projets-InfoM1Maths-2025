#!/bin/bash

# Le code marche très bien, le temps d'execution à afficher

read -p "entrer n: " n
read -p "entrer mod m: " m
echo "***Table de multiplication modulaire de $n mod $m***"
for ((i=1; i<=10; i++));
do
resultat=$((i * n))
echo "        $i*$n=$((resultat%m))"
done
