# Chiffrement par décalage de 3

Ce script permet de **chiffrer** et **déchiffrer** un texte en utilisant un décalage de 3 positions dans un alphabet défini. Il gère à la fois les lettres minuscules et majuscules et laisse inchangés les caractères qui ne figurent pas dans l'alphabet.

## Fonctionnement

- **Chiffrement** : Chaque lettre du texte est remplacée par celle située 3 positions plus loin dans l'alphabet. Si la fin de l'alphabet est atteinte, le décalage continue depuis le début.
- **Déchiffrement** : Chaque lettre du texte est remplacée par celle située 3 positions en arrière, permettant ainsi de retrouver le texte original.

## Utilisation

1. **Exécution du script**  
   Lancez le script avec la commande suivante :
   ```bash
   python3 chiffrement_simple.py
## EXEMPLE

"La vie est belle." devient "Od ylh hvw ehooh".


