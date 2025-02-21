#!/bin/bash
echo "Algorithme d'Euclide et identité de Bezout: "
function euclide()
{
    a=$1
    b=$2
    let "r=$a%$b"
    u=1
    v=0
    s=0
    t=1
until [ $r -eq  0 ];do
    let "q=$a/$b"
    let "u=$u-$s*$q"
    let "v=$v-$t*$q"
    tempo=$s
    s=$u
    u=$tempo
    tempo=$t
    t=$v
    v=$tempo
    a=$b
    b=$r
    let "r=$a%$b"
done
        echo "LE PGCD de $1 et de $2  est $b . "
echo "On a $1 * $s + $2 * $t = $b . "
}
read -p "Entrer un nombre entier relatif que vous vouler: " m
read -p "Entrer un autre nombre:  " n
let "deb=$(date +%s%N)"
euclide $m $n
let "fin=$(date +%s%N)"
let "dur=$fin-$deb"
echo "Le calcul a duré $dur nanosecondes. "
