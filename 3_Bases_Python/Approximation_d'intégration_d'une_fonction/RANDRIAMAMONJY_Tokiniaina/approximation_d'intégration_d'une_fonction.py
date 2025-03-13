import numpy as np
def f(x):
    return x**2 
def monte_carlo_integral(n_points):
    x = np.random.uniform(0, 1, n_points) 
    fx = f(x)  
    integral_approx = np.mean(fx) 
    return integral_approx, x, fx
valeur_exacte = 1/3  
n_points = 1000000
integral_approx, x_points, fx_points = monte_carlo_integral(n_points) 
# Calcul de l'erreur 
erreur = abs(valeur_exacte - integral_approx) 
print(f"Approximation de l'intégrale avec {n_points} points : {integral_approx:.6f}")
print(f"Valeur exacte : {valeur_exacte:.6f}") 
print(f"Erreur absolue : {erreur:.6f}") 