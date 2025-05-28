
import matplotlib.pyplot as plt

# Fonction qui calcule le n-ième terme de la suite de Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Calcul des 20 premiers termes de la suite de Fibonacci
n_terms = 20
fib = [fibonacci(i) for i in range(n_terms)]

# Affichage des 20 premiers termes
print("Les 20 premiers termes de la suite de Fibonacci:")
print(fib)

# Visualisation graphique de la suite
#cree une nouvelle figure
plt.figure(figsize=(10, 6))
#tracer la courbe
plt.plot(range(n_terms),fib, marker='o', color='b', label='Suite de Fibonacci')
plt.title('Suite de Fibonacci (20 premiers termes)')
plt.xlabel('Index')
plt.ylabel('Valeur')
plt.legend()
plt.grid(True)
#affiche la figure
plt.show()

# Analyse du comportement asymptotique
# La suite de Fibonacci croît de manière exponentielle, environ comme phi^n / racine(5)
phi = (1 + 5 ** 0.5) / 2  # Nombre d'or
asymptotic_growth = [phi ** i / (5 ** 0.5) for i in range(n_terms)]

# Affichage de la croissance asymptotique
plt.figure(figsize=(10, 6))
plt.plot(range(n_terms), fib, marker='o', label='Suite de Fibonacci')
plt.plot(range(n_terms), asymptotic_growth, '--', label='Croissance asymptotique (phi^n / sqrt(5))')
plt.title('Croissance de la suite de Fibonacci et de sa forme asymptotique')
plt.xlabel('Index')
plt.ylabel('Valeur')
plt.legend()
plt.grid(True)
plt.show()
