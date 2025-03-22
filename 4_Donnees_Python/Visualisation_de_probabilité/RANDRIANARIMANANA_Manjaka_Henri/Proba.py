import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=(9, 4))# Taille réduite pour écran mobile
# Paramètres
n_lancers = 1000 
n_faces = 6
# Simulation
lancers = np.random.randint(1, n_faces + 1, size=n_lancers)
proba_exp = np.bincount(lancers)[1:] / n_lancers
proba_theo = np.full(n_faces, 1/n_faces)
# Graphique
plt.bar(range(1, n_faces + 1), proba_exp, alpha=0.7, label='Expérimental', color='blue')
plt.plot(range(1, n_faces + 1), proba_theo, 'r-', label='Théorique', marker='o')
plt.xlabel('Face')
plt.ylabel('Probabilité')
plt.title(f'{n_lancers} lancers')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
# Stats
print(f"Total lancers : {n_lancers}")
print("Probabilités expérimentales :", proba_exp)
print("Probabilité théorique :", 1/n_faces)
