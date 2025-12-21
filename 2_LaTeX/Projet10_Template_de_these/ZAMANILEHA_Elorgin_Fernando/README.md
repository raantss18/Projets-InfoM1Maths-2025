# Template de Thèse en LaTeX

Un template moderne et professionnel pour rédiger une thèse en français, conforme aux standards universitaires.

## Fonctionnalités

- Structure prête à l'emploi avec page de titre, table des matières, chapitres et bibliographie
- Configuration pour le français (polices, typographie, babel)
- Mise en page élégante avec des marges appropriées
- Prise en charge des équations mathématiques (amsmath)
- Gestion des références bibliographiques (natbib)
- Hyperliens dans le PDF final (hyperref)

## Prérequis

- Distribution LaTeX récente (TeX Live 2023+, MikTeX 21+)
- Compilation avec pdflatex (ou lualatex/xelatex)

## Utilisation

1. Cloner ou télécharger ce dépôt
2. Modifier les variables dans le préambule (titre, auteur, etc.)
3. Remplacer `logo-univ.png` par votre logo d'université
4. Ajouter vos chapitres dans le fichier principal
5. Compiler avec :
   ```bash
   pdflatex main.tex
   bibtex main
   pdflatex main.tex
   pdflatex main.tex