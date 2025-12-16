Ce projet analyse l'impact des habitudes de vie des étudiants (temps d'écran, sommeil, activité physique) sur le **stress**, l'**anxiété avant les examens** et la **performance académique**, à l'aide de modèles de **machine learning**. Il inclut également un **système de recommandations** basé sur des simulations d'interventions comportementales.

## 📁 Contenu du projet

- `Student_stress_performance_prediction_recomandation.ipynb`
  - Notebook principal contenant :
    - l'analyse exploratoire des données (EDA),
    - le prétraitement et l'encodage des variables,
    - l'entraînement et l'évaluation de plusieurs modèles ML,
    - une fonction de recommandation basée sur des modifications de variables comportementales.

- `rapport_student_stress_performance.tex`
  - Rapport scientifique en LaTeX décrivant la méthodologie, les résultats et les recommandations.

- `README.md`
  - Description générale du projet (ce fichier).

## 🎯 Objectifs

1. Prédire le **niveau de stress** des étudiants.
2. Prédire la **variation de la performance académique**.
3. Utiliser les modèles entraînés pour proposer des **recommandations personnalisées** visant à :
   - réduire le stress,
   - améliorer ou stabiliser la performance académique.

## 📊 Données utilisées

Le jeu de données contient des informations anonymisées par étudiant, notamment :

- Données démographiques : genre, âge, niveau d'éducation.
- Habitudes de vie :
  - temps d'écran quotidien (heures/jour),
  - durée de sommeil (heures/nuit),
  - activité physique (heures/semaine).
- Indicateurs cibles :
  - niveau de stress (Low / Medium / High),
  - anxiété avant les examens,
  - changement de performance académique.

## ⚙️ Méthodologie

### 1. Prétraitement
- Suppression des colonnes non pertinentes ou identifiantes.
- Conversion des variables numériques.
- Encodage des variables catégorielles.
- Séparation train / validation / test.

### 2. Modélisation

Les modèles suivants sont entraînés et comparés :

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)
- Naive Bayes

Les performances sont évaluées à l'aide de :
- Accuracy
- Précision
- Rappel
- Score F1
### lien du CSV : https://www.kaggle.com/datasets/utkarshsharma11r/student-mental-health-analysis&ved=2ahUKEwjR64eFnMORAxW_Y0EAHeWQDl0QFnoECBcQAQ&usg=AOvVaw0s0s6EkDIO1OrQRnPsQv0L


