
import random

# Fonction à intégrer
def f(x):
    return x**2

# Fonction pour calculer l'intégrale de Monte-Carlo
def monte_carlo_integration(func, a, b, num_samples):
    T = 0
    for _ in range(num_samples):
        x = random.uniform(a, b)  # Tirage aléatoire de x entre a et b
        T += func(x)  # Somme des évaluations de la fonction
    # Calcul de l'intégrale approchée 
    return (b - a) * T / num_samples

# Paramètres
a = 0
b = 1
num_samples = 100000  # Nombre d'échantillons


# Calcul de l'intégrale approchée pour la fonction choisie avec les parametres données
approximation = monte_carlo_integration(f, a, b, num_samples)

# Valeur exacte de l'intégrale (b³-a³)/3
exact_value = 1 / 3

# Calcul de l'erreur 
error = abs(approximation - exact_value)

# Affichage des résultats
print(f"la valeur de l'integrale approché est : {approximation}")
print(f"la Valeur exacte de l'integrale est : {exact_value}")
print(f"l'erreur à la valeur exacte est : {error}")
print("En augmentant num_samples(le nombre d'echantillons), l'approximation de l'intégrale devrait devenir de plus en plus précise")
