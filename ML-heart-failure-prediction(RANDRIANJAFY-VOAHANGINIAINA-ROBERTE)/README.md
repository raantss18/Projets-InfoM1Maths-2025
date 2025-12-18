# 🏥 Prédiction de la Mortalité par Insuffisance Cardiaque

Ce projet implémente un pipeline complet de Machine Learning pour prédire le risque de décès chez les patients atteints d'insuffisance cardiaque. Il compare plusieurs familles d'algorithmes et optimise les meilleurs modèles pour garantir une fiabilité médicale maximale.

## 📋 Description du Dataset
Le jeu de données contient **299 patients** avec 13 caractéristiques cliniques. La cible est la colonne `DEATH_EVENT` (1 si le patient est décédé, 0 sinon).

Les variables clés incluent :
- **Facteurs biochimiques :** Créatinine phosphokinase, Fraction d'éjection, Plaquettes, Créatinine sérique, Sodium sérique.
- **Facteurs de risque :** Âge, Anémie, Diabète, Hypertension, Sexe, Tabagisme.

## 🛠️ Stack Technique
- **Langage :** Python
- **Traitement de données :** `Pandas`, `NumPy`
- **Modélisation :** `Scikit-learn`, `XGBoost`, `LightGBM`
- **Gestion du déséquilibre :** `Imbalanced-learn` (SMOTE)
- **Visualisation :** `Matplotlib`, `Seaborn`

## 🚀 Fonctionnement du Code

Le script est divisé en plusieurs étapes logiques :

1. **Prétraitement :** Nettoyage des doublons et pipeline de transformation (Imputation + Standardisation).
2. **Architecture Baseline :** Évaluation de 8 modèles (Régression Logistique, KNN, SVM, Random Forest, Extra Trees, Gradient Boosting, XGBoost, LightGBM).
3. **Optimisation :** Tuning des hyperparamètres sur le Top-3 des modèles via `RandomizedSearchCV`.
4. **Refit & Test :** Ré-entraînement sur les données combinées (Train + Validation) et évaluation finale sur le set de Test (20%).
5. **Exports :** Génération automatique de graphiques (ROC, Confusion Matrix) et de fichiers CSV de synthèse.



## 📊 Performance & Métriques
Le projet met l'accent sur trois métriques cruciales pour le domaine médical :
- **Recall (Sensibilité) :** Pour minimiser les faux négatifs (ne pas rater un patient à risque).
- **ROC AUC :** Pour évaluer la capacité globale de séparation des classes.
- **F1-Score :** Pour équilibrer la précision et la détection.


