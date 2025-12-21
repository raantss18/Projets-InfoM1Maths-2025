#!/bin/bash
is_perfect_square() {
    local N=$1
    
    local sqrt_N=$(echo "sqrt($N)" | bc)
    
    if (( sqrt_N * sqrt_N == N )); then
        return 0 
    else
        return 1 
    fi
}
fermat_factorization() {
    local N=$1
    if (( N % 2 == 0 )); then
        echo "Facteur trouvé: 2 et $(( N / 2 ))"
        return
    fi

    local x=$(echo "sqrt($N)" | bc) 

    if (( x * x < N )); then
        (( x++ ))
    fi

    local y2 y

    while true; do
        y2=$(( x * x - N ))

        if is_perfect_square "$y2"; then
            y=$(echo "sqrt($y2)" | bc)
            break
        fi

        (( x++ ))
    done

    # Calcul des facteurs
    local factor1=$(( x - y ))
    local factor2=$(( x + y ))

    echo "Facteurs trouvés: $factor1 et $factor2"
}

# Vérification
if [ $# -ne 1 ]; then
    echo "Usage: $0 <nombre à factoriser>"
    exit 1
fi

N=$1
fermat_factorization "$N"
#temps d'execution
time fermat_factorization $N


#factorisation methode naive
naive_factorization() {
    local N=$1
    echo "Facteurs de $N:"
    for ((i=2 ; i*i <= N ; i++)); do
    	while (( N % i == 0 )); do
             echo "Facteur trouver : $i"
             N=$((N / i))
         done
    done
    if ((N > 1)); then
   	 echo "Facteur trouver : $N"
    fi
    	echo
}
# Vérification
if [ $# -ne 1 ]; then
    echo "Usage: $0 <nombre à factoriser>"
    exit 1
fi

N=$1
naive_factorization "$N"
#temps d'execution
time naive_factorization $N





