``` markdown
## 📑 Projet Exercice 12 - Estimation pour loi de Poisson  
**Livrables : Code Jupyter + Rapport PDF**  

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)
![LaTeX](https://img.shields.io/badge/LaTeX-Rapport-white)

## 🗂 Structure du projet
``` 
```plaintext
projet_exercice12/
├── code.ipynb            # Notebook complet (simulations + analyses)
├── rapport.pdf           # Rapport final compilé (PDF)
├── rapport.tex           # Sources LaTeX
├── figures/              # Graphiques PDF générés
│   ├── convergence.pdf
│   ├── mse_plot.pdf
│   └── biais_variance.pdf
└── README.md             
``` 
## 🚀 Guide d'utilisation
Prérequis
Python 3.8+ avec numpy, matplotlib, jupyter

Distribution LaTeX complète

Installation
Clonez le dépôt :

``` bash
git clone https://github.com/raantss18/Projets-InfoM1Maths-2025/projet_exercice12.git
cd projet_exercice12
``` 
Installez les dépendances :

``` bash
pip install numpy matplotlib jupyter
sudo apt install texlive-latex-extra texlive-fonts-recommended
``` 
Utilisation
Lancer le notebook :

``` bash
jupyter notebook code.ipynb
Exécutez toutes les cellules pour régénérer les figures
``` 
Compiler le rapport :

``` bash
pdflatex rapport.tex
pdflatex rapport.tex  # 2e compilation pour les références
``` 
## 📝 Contenu clé
Dans code.ipynb :
Simulation des échantillons (MLE, Bayes, Tronqué)

Calculs empiriques (biais, variance, MSE)

Génération automatique des figures

Dans rapport.tex :
Partie théorique :

Borne de Cramér-Rao

Propriétés des estimateurs

Résultats :

Comparaison des performances

Visualisations des figures

🔍 Comment contribuer
Modifiez code.ipynb pour de nouvelles analyses

Mettez à jour rapport.tex avec vos conclusions

Régénérez les figures et le PDF

## 📧 Contact
Auteur : RANDRIANJAFY Voahanginiaina Roberte
Email : niainaroberte@gmail.com

*© 2024 - MIT License