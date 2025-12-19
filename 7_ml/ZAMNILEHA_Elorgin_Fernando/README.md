# Projet : Détection de Fraude aux Cartes de Crédit

## Description du projet
Ce projet vise à détecter les transactions frauduleuses par carte de crédit à l'aide de techniques d'apprentissage automatique. Il repose sur un jeu de données synthétique de 10 000 transactions contenant plusieurs features pertinentes (montant, heure, catégorie marchand, etc.) et une variable cible binaire `is_fraud`.

Huit modèles de classification ont été entraînés, optimisés et comparés :  
- Logistic Regression  
- Decision Tree  
- Random Forest  
- Gradient Boosting  
- AdaBoost  
- Extra Trees  
- SVM  
- K-Nearest Neighbors  

Le modèle **AdaBoost** obtient les meilleures performances avec un score parfait (Accuracy = 1.0, F1-Score = 1.0, ROC-AUC = 1.0) sur l'ensemble de test.

## Structure du repository

```
.
├── credit_card_fraud_10k.csv          # Jeu de données (10 000 transactions)
├── model_comparison_results_sklearn.csv # Résultats détaillés des modèles
├── performance.ipynb                  # Notebook Jupyter complet (analyse, entraînement, visualisation)
├── images/
│   ├── importance_des_features_adaboost.png     # Importance des features (AdaBoost)
│   ├── comparaison_des_performances_des_modeles.png # Comparaison multi-métriques
│   └── radar_chart_top_3_modeles.png            # Radar chart des 3 meilleurs modèles
├── rapport_analyse_fraude.pdf         # Rapport complet au format PDF (optionnel)
└── README.md                          # Ce fichier
```

## Aperçu des données (`credit_card_fraud_10k.csv`)

Colonnes :
- `transaction_id` : ID unique
- `amount` : Montant de la transaction
- `transaction_hour` : Heure de la transaction (0-23)
- `merchant_category` : Catégorie du marchand (Electronics, Travel, Grocery, Food, Clothing)
- `foreign_transaction` : Transaction à l'étranger (0/1)
- `location_mismatch` : Incohérence géographique (0/1)
- `device_trust_score` : Score de confiance du dispositif
- `velocity_last_24h` : Nombre de transactions dans les dernières 24h
- `cardholder_age` : Âge du titulaire
- `is_fraud` : Cible - fraude (0/1)

**Caractéristiques** :
- 10 000 lignes
- Aucun valeur manquante
- Classe fortement déséquilibrée (~0.3 % de fraudes)

## Résultats principaux

| Modèle               | Accuracy | Precision | Recall | F1-Score | ROC-AUC | Temps entraînement (s) |
|----------------------|----------|-----------|--------|----------|---------|------------------------|
| **AdaBoost**         | **1.0000** | **1.0000** | **1.0000** | **1.0000** | **1.0000** | 264.77 |
| Gradient Boosting    | 0.9995   | 0.9677    | 1.0000 | 0.9836   | 1.0000  | 717.00 |
| Decision Tree        | 0.9995   | 0.9677    | 1.0000 | 0.9836   | 0.9997  | 6.02   |
| Random Forest        | 0.9940   | 1.0000    | 0.6000 | 0.7500   | 0.9999  | 86.18  |
| Extra Trees          | 0.9940   | 0.7500    | 0.9000 | 0.8182   | 0.9981  | 358.16 |
| SVM                  | 0.9915   | 0.6757    | 0.8333 | 0.7463   | 0.9942  | 1128.85|
| K-Nearest Neighbors  | 0.9875   | 0.6190    | 0.4333 | 0.5098   | 0.8948  | 40.65  |
| Logistic Regression  | 0.9585   | 0.2655    | 1.0000 | 0.4196   | 0.9927  | 122.45 |

**Conclusion** : AdaBoost est le modèle le plus performant et le plus stable (CV Mean F1 ≈ 0.996).

## Features les plus importantes (AdaBoost)
1. `transaction_hour`
2. `foreign_transaction`
3. `device_trust_score`
4. `location_mismatch`
5. `velocity_last_24h`

## Comment exécuter le projet

1. Cloner le repository
2. Installer les dépendances :
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn jupyter
   ```
3. Lancer le notebook :
   ```bash
   jupyter notebook performance.ipynb
   ```

Le notebook contient toutes les étapes : chargement, prétraitement, entraînement, optimisation des hyperparamètres (GridSearchCV), évaluation et visualisations.

## Visualisations incluses
- Bar plot de l'importance des features
- Comparaison multi-métriques des modèles (F1, ROC-AUC, temps, validation croisée)
- Radar chart des 3 meilleurs modèles
- Heatmap des performances

## Auteur
Analyse réalisée avec l'assistance de Grok 4 (xAI) - Décembre 2025

## Licence
Libre d'utilisation à des fins éducatives et de recherche.