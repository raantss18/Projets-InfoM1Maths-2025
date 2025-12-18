#!/bin/bash

Suite_de_Fibonacci() {
n=$1
if [ "$n" -le 0 ]; then
   echo "F($n)= 0"
   return
elif [ "$n" -eq 1 ]; then
     echo "F($n)= 1"
     return
fi
   echo "F(1)= 1"
   a=0
   b=1
   for ((i=2;i<=n;i++)) do
       c=$((a+b))
       a=$b
       b=$c
       echo "F($i)= $b"
   done
}

read -p " Entrer le rang de la suite: " rang
Suite_de_Fibonacci "$rang" | tee Fibonacci.txt
  