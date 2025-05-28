 # Statistiques sur un ensemble de données

On a importé les bibliothèques pandas pour la manipulation et analyse des données,matplotlib pour la visualisation basique des données et seaborn pour une visualisation stylisée puis un fichier csv contenant toutes les données et on a selectionné les colonnes numeriques .

On calcule la moyenne pour chaque variable,la variance et la mediane. On a montré par un schema la distribution pour 2 variables.

`data=pd.read_csv("ambondrona.csv")`lit le fichier ambondrona.csv

 ## Conversion en DataFrame avec renommage de colonne

`.to_frame(name="Moyenne")` convertit la Série en DataFrame avec une colonne nommée "Moyenne".

`.reset_index()` remet les noms des colonnes en place et transforme les index en une colonne.

`.columns = ["Catégorie", "Valeur Moyenne"]` définit le nom des colonnes

 ## Création de la figure
`plt.figure(figsize=(10, 4))` Initialise une figure matplotlib avec sa taille

`for i, var in enumerate(variables):` enumerate(variables) permet de boucler sur les variables et d’obtenir :

  - i : l’index (0 pour "Plastique", 1 pour "Revenus par mois")
  - var : le nom de la variable (ex. "Plastique")
    
`plt.subplot(1, 2, i+1)` Crée un subplot (graphe) dans une grille de 1 ligne et 2 colonnes.Le i+1 définit la position du graphique :
   - Si i=0, ça affiche le premier graphe.
   - Si i=1, ça affiche le deuxième graphe
     
`sns.histplot(data[var], bins=30, kde=True, color="blue")` sns.histplot() crée un histogramme pour data[var] avec :
   - bins=30 : Sépare les valeurs en 30 intervalles.
   - kde=True : Ajoute une courbe de densité (Kernel Density Estimation).
   - color="blue" : Histogramme en bleu.
     
`plt.title(f"Distribution de {var}")` définit le titre

`plt.xlabel(var)` définit le nom de l'axe x

`plt.ylabel("Valeur")` définit le nom de l'axe y

`plt.tight_layout()` Ajuste la mise en page pour éviter que les graphiques se chevauchent.

