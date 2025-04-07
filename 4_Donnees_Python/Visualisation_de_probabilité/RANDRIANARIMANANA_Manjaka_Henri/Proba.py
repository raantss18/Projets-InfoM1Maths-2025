import matplotlib.pyplot as plt
nb_lancers = 1000  # Nombre total de lancers
nb_faces = 6      # Nombre de faces du dé
resultats = [(i % nb_faces) + 1 for i in range(nb_lancers)]
# Créer l'histogramme
plt.figure(figsize=(10, 6))
plt.hist(resultats, bins=range(1, nb_faces + 2), align='left', rwidth=0.8, color='skyblue')
# Personnaliser le graphique
plt.title(f'Distribution de {nb_lancers} "lancers" d\'un dé à {nb_faces} faces')
plt.xlabel('Résultat')
plt.ylabel('Nombre d\'occurrences')
plt.xticks(range(1, nb_faces + 1))
plt.grid(True, alpha=0.3)
# Afficher le graphique
plt.show()
# Compter les occurrences
frequences = [resultats.count(i) for i in range(1, nb_faces + 1)]
print("\nNombre d'occurrences par face:")
for i, freq in enumerate(frequences, 1):
    print(f"Face {i}: {freq}")
