import csv 
import matplotlib
matplotlib.use('TkAgg')  # pour éviter le bug "qt.qpa.plugin: Could not find the Qt platform plugin "wayland" in ""
import matplotlib.pyplot as plt

x_points = []
y_points = []

#lis les points du fichier csv
with open('points.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)  # ignore l'entête
    for row in reader:
        x_points.append(float(row[0]))
        y_points.append(float(row[1]))
#affiche les couples (x,y)
print("les points du fichier csv sont:")
for x, y in zip(x_points, y_points):
    print(f"({x}, {y})")

#crée un liste de points en y pour trouver les coefficients du polynome
y_p = y_points.copy()

#créeation d'une matrice de vandermonde pour trouver les coefficients du polynome
Vandermonde_matrice = [[x**i for i in range(len(x_points))] for x in x_points]

#utilisation de l'algorithme de gauss pour obtenir une matrice triangulaire et change les valeurs de y_p en conséquence
for j in range(len(x_points)):
    for i in range(j+1, len(x_points)):
        factor = Vandermonde_matrice[i][j] / Vandermonde_matrice[j][j]
        for k in range(len(x_points)):
            Vandermonde_matrice[i][k] -= factor * Vandermonde_matrice[j][k]
        y_p[i] -= factor * y_p[j]

#definition des coefficients du polynome
coefficients = [0]*len(x_points)

#calcul des coefficients du polynome
for i in range(len(x_points)-1, -1, -1):
    coefficients[i] = y_p[i] / Vandermonde_matrice[i][i] - sum(Vandermonde_matrice[i][j] * coefficients[j] for j in range(i+1, len(x_points))) / Vandermonde_matrice[i][i]
#definition de la fonction polynome
def polynome(x):
    return sum(coefficients[i] * x**i for i in range(len(x_points)))

#affichage de l'expression du polynome
polynome_str = " + ".join(
    [
        f"{coefficients[i]:.2f}" if i == 0 else
        (f"{coefficients[i]:.2f}*x" if i == 1 else f"{coefficients[i]:.2f}*x^{i}")
        for i in range(len(x_points))
    ]
)
print("\nL'expression du polynôme d'interpolation est :")
print("P(x) = ", polynome_str)

# Création d'une suite dense de points pour tracer la courbe 
x_min, x_max = min(x_points) - 1, max(x_points) + 1
x_axe = [x_min + i * (x_max - x_min) / 999 for i in range(1000)]
y_axe = [polynome(xi) for xi in x_axe]

# --- Affichage des points et de la courbe interpolée ---
plt.figure(figsize=(8, 8))
plt.scatter(x_points, y_points, color='red', label='Points')
plt.plot(x_axe, y_axe, color='blue', label="Polynôme d'interpolation")
plt.title("Interpolation par polynôme")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
