import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(points, x_eval):
    """
    Calcule l'interpolation de Lagrange pour les points donnés et évalue à x_eval.
    points: liste de tuples [(x0, y0), (x1, y1), ...]
    x_eval: points où évaluer le polynôme
    """
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    n = len(points)
    
    # Calcul de L(x) pour chaque x_eval
    result = []
    for x_val in x_eval:
        L_x = 0
        for i in range(n):
            term = y[i]
            for j in range(n):
                if j != i:
                    term *= (x_val - x[j]) / (x[i] - x[j])
            L_x += term
        result.append(L_x)
    
    return np.array(result)

# Exemple d'entrée : ensemble de points (x, y)
points = [(0, 1), (1, 0), (2, 3), (3, 5)]

# Points pour évaluer le polynôme (pour un tracé lisse)
x_plot = np.linspace(min([p[0] for p in points]), max([p[0] for p in points]), 100)
y_plot = lagrange_interpolation(points, x_plot)

# Tracé
plt.figure(figsize=(8, 6))
plt.plot(x_plot, y_plot, 'b-', label='Polynôme de Lagrange')
plt.scatter([p[0] for p in points], [p[1] for p in points], color='red', label='Points donnés')
plt.title('Interpolation de Lagrange')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.savefig('lagrange_interpolation.png')
plt.show()