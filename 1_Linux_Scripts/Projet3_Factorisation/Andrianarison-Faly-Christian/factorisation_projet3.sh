#!/bin/bash

echo "          *****************"
echo "          * FACTORISATION *"
echo "          *****************"

function factorisation_naive()
{
    a=$1
    b=2
    until [ $(($a / $b)) -lt $b ]; do
        if [ $(($a % $b)) -eq 0 ]; then
            echo " ==> $n = $b * $(($a/$b))"
            exit 0
        fi
        b=$(($b+1))
    done
    echo "$n est un nombre premier."
}

function produit_de_premiers()
{
    local n=$1; local a=$n;
    local premiers=("2" "3")
    local decomposition="1"
    local p=1

    until [ $a -eq 1 ]; do
        #générer les nombres premiers un par un (un par itération)
        if [ $p -gt 2 ]; then
            nbr_premier_trouvE="false"
            until $nbr_premier_trouvE; do
                p=$(($p + 2))
                for q in ${premiers[@]}; do
                    if [ $(($p % $q)) -eq 0 ]; then 
                        break
                    elif [ $(($p / $q)) -lt $q ]; then   
                        nbr_premier_trouvE="true"
                        premiers+=("$p")
                        break
                    fi
                done
            done
        else p=$(($p + 1))
        fi
        #echo $p

        #test de divisibilité de a par p
        if [ $(($a % $p)) -eq 0 ]; then
            local exposant=0
            while [ $(($a % $p)) -eq 0 ]; do
                exposant=$(($exposant + 1))
                a=$(($a / $p))
            done
            if [ $exposant -eq 1 ]; then 
                decomposition="${decomposition} * $p"
            else 
                decomposition="${decomposition} * $p^$exposant"
            fi
        elif [ $(($a / $p)) -lt $p ]; then
            decomposition="${decomposition} * $a"
            a=1
        fi

    done

    #echo ${premiers[@]}
    echo "==> $n = $decomposition"
    #exit 0
}

until [[ $n =~ ^[0-9]+$ ]] && [ $n -ge 2 ]; do
    read -p "Veuillez entrer un nombre entier superieur a 2: >" n
    if [[ $n =~ ^[0-9]+$ ]] && [ $n -ge 2 ]; then
        echo "En cours..."
    else 
        echo "Erreur: mauvaise entrée !"
    fi
done

start_time=$(date +%s)

produit_de_premiers $n

end_time=$(date +%s)
echo "(execution_time: $((end_time - start_time))s)"
