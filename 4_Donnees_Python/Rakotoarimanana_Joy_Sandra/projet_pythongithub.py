import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_csv("ambondrona.csv")
numerique=data.select_dtypes(include=["number"])#selectionne seulement les colonnes numériques
moyenne=numerique.mean()#calcule la moyenne pour chaque colonne numerique
moyenne_df = moyenne.to_frame(name="Moyenne").reset_index()
moyenne_df.columns = ["Catégorie", "Valeur Moyenne"]#définit les noms pour les colonnes

variance=numerique.var()#calcule la variance pour chaque colonne numerique
variance_df = variance.to_frame(name="Variance").reset_index()
variance_df.columns = ["Catégorie", "Variance"]

mediane=numerique.median()#calcule la mediane pour chaque colonne numerique
mediane_df = mediane.to_frame(name="Mediane").reset_index()
mediane_df.columns = ["Catégorie", "Mediane"]

print("voici la moyenne pour chaque categorie\n")
print(moyenne_df,"\n")
print("Voici la variance pour chaque categorie\n")
print(variance_df,"\n")
print("voici la mediane pour chaque categorie\n")
print(mediane_df,"\n")

#distribution pour les variables
variables = ["Plastique","Revenus par mois"]
plt.figure(figsize=(10, 4))
for i, var in enumerate(variables):
    plt.subplot(1, 2, i+1)
    sns.histplot(data[var], bins=30, kde=True, color="blue")
    plt.title(f"Distribution de {var}")
    plt.xlabel(var)
    plt.ylabel("Valeur")
plt.tight_layout()
plt.show()#affiche la figure




