from math import pi
from random import random

def MonteCarlo(prec):
    """
    Méthode d'approximation de PI par Monte Carlo
    
        prec:int => "erreur inférieure à 10^(-prec)"
    """
    PI_approx = 0
    N = 0 # nombre d'itérations
    N_in = 0 # Nombre de points tombés dans le quart de disque
    while (abs(pi - PI_approx) >= 0.1**prec):
        N += 1; x, y = random(), random()
        if x**2 + y**2 <= 1:
            N_in += 1; 
        PI_approx = 4 * (N_in / N)
    return PI_approx, N

def show_error(N):
    """
    Visualiser l'erreur en fonction du nombre d'itération

        N:int => nombre d'itération
    """
    import matplotlib.pyplot as plt
    
    iter = [i for i in range(N)]  # 0 à N-1
    err = [] 
    
    PI_approx = 0
    N_in = 0 # Nombre de points tombés dans le quart de disque
    for n in iter:
        x, y = random(), random()
        if x**2 + y**2 <= 1:
            N_in += 1; 
        PI_approx = 4 * (N_in / (n+1))
        error = abs(pi - PI_approx)
        err.append(error)
        
    plt.plot(iter, err)
    plt.title("Représentation de l'erreur d'approximation")
    plt.xlabel("nombre d'itérations")
    plt.ylabel("erreur")
    plt.show()

    print(f"La valeur approximative de PI après {N} itérations est: {PI_approx}")
    print(f"Erreur: {error}")



if __name__ == "__main__":
    print("\u2500"*80, "\n", "APPROXIMATION DE PI PAR LA MÉTHODE Monte Carlo")
    print("Ce programme demande à l'utilisateur le nombre d'itérations pour faire l'approximation; puis renvoie l'approximation de PI avec l'erreur correspondante et affiche la courbe de l'erreur en fonction du nombre d'itérations.")
    print("\u2500"*80)
    ##############################################""
    N = ""
    while type(N) != int:
        try: N = int(input("=> Entrer le nombre d'itérations: "))
        except ValueError: 
            print("Veuillez entrer un nombre entier !")
    show_error(N)