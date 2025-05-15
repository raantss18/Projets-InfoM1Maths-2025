import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time

def monte_carlo_pi(n_samples, n_points_per_sample, show_all_points=False):
    """Approximation de π par la méthode de Monte Carlo avec visualisation des points"""
    estimates = []
    inside = 0
    total_points = 0
    
    # Création de la figure
    plt.figure(figsize=(15, 6))
    
    # Graphique des points
    ax1 = plt.subplot(1, 2, 1)
    square = patches.Rectangle((-1, -1), 2, 2, linewidth=1, edgecolor='black', facecolor='none')
    circle = patches.Circle((0, 0), 1, linewidth=1, edgecolor='red', facecolor='none')
    ax1.add_patch(square)
    ax1.add_patch(circle)
    ax1.set_xlim(-1.1, 1.1)
    ax1.set_ylim(-1.1, 1.1)
    ax1.set_aspect('equal')
    ax1.set_title(f'Points aléatoires (0/{n_samples*n_points_per_sample})')
    
    # Graphique de convergence
    ax2 = plt.subplot(1, 2, 2)
    ax2.axhline(y=np.pi, color='r', linestyle='--', label='Valeur réelle de π')
    ax2.set_xlabel('Nombre de points')
    ax2.set_ylabel('Estimation de π')
    ax2.set_title('Convergence de l\'estimation')
    ax2.legend()
    ax2.grid(True)
    
    plt.tight_layout()
    plt.ion()  # Mode interactif
    plt.show()
    
    for i in range(n_samples):
        # Générer des points aléatoires
        x = np.random.uniform(-1, 1, n_points_per_sample)
        y = np.random.uniform(-1, 1, n_points_per_sample)
        
        # Calculer quels points sont dans le cercle
        distances = x**2 + y**2
        in_circle = distances <= 1
        inside += np.sum(in_circle)
        total_points += n_points_per_sample
        
        # Estimation de π
        pi_estimate = 4 * inside / total_points
        estimates.append(pi_estimate)
        
        # Affichage des points
        if show_all_points:
            # Afficher tous les points depuis le début
            ax1.scatter(x[in_circle], y[in_circle], color='blue', s=1, alpha=0.3)
            ax1.scatter(x[~in_circle], y[~in_circle], color='green', s=1, alpha=0.3)
        else:
            # Afficher seulement les nouveaux points
            ax1.clear()
            ax1.add_patch(square)
            ax1.add_patch(circle)
            ax1.scatter(x[in_circle], y[in_circle], color='blue', s=3, alpha=0.5)
            ax1.scatter(x[~in_circle], y[~in_circle], color='green', s=3, alpha=0.5)
        
        ax1.set_title(f'Points aléatoires ({total_points}/{n_samples*n_points_per_sample})')
        
        # Mise à jour du graphique de convergence
        ax2.plot(np.arange(1, len(estimates)+1) * n_points_per_sample, estimates, 'b-')
        
        plt.draw()
        plt.pause(0.05)  # Pause courte pour permettre la mise à jour
    
    plt.ioff()  # Désactive le mode interactif
    plt.tight_layout()
    plt.show()
    
    return pi_estimate, estimates

# Paramètres
n_samples = 80        # Nombre d'échantillons
n_points_per_sample = 200  # Points par échantillon

# Exécution avec affichage de tous les points
pi_estimate, estimates = monte_carlo_pi(n_samples, n_points_per_sample, show_all_points=True)
print(f"Estimation finale de π: {pi_estimate}")
print(f"Erreur relative: {abs(pi_estimate - np.pi)/np.pi * 100:.4f}%")