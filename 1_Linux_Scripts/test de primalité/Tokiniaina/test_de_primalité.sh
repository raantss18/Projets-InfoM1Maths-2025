#!/bin/bash

# A revoir, le code s'execute avec erreur et ne donne pas le résultat attendu.

primality_of() {
    local n=$1

    # verification if the number entered by  user is really a Natural integer
    if ! [[ "$n" =~ ^[0-9]+$ ]]; then
        echo "Error: Please enter a positive integer."
        return 1
    fi

    if (( n < 2 )); then
        echo "$n isn’t a prime number."
        return
    fi

    if (( n == 2 )); then
        echo "$n is a prime number."
        return
    fi

    if (( n % 2 == 0 )); then
        echo "$n isn’t a prime number."
        return
    fi

    # limite calculation for the  divisor 
    limdiv=$(echo "sqrt($n)" | bc)

    for (( i=3; i<=limdiv; i+=2 )); do
        if (( n % i == 0 )); then
            echo "$n isn’t a prime number."
            return
        fi
    done

    echo "$n is a prime number."
}

# Asking for the user to enter his number
read -p "Enter a number to test its primality: " nombre

# called the function that have been enter
primality_of "$nombre"

