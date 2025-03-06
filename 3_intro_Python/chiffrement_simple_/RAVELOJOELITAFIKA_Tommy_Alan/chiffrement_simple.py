# Ce programme utilise le décalage de 3 dans l'alphabet pour chiffrer et déchiffrer un texte

ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def chiffrer(texte):
    c = ''
    for i in texte:
        if ALPHABET.find(i) == -1:  # vérifie si le caractère est dans l'alphabet défini
            c += i                # s'il ne l'est pas, on le laisse tel quel
        else:
            c += ALPHABET[(ALPHABET.find(i) + 3) % len(ALPHABET)]
    return c

def dechiffrer(texte):
    e = ''
    for i in texte:
        if ALPHABET.find(i) == -1:  # vérifie si le caractère est dans l'alphabet défini
            e += i                # s'il ne l'est pas, on le laisse tel quel
        else:
            e += ALPHABET[(ALPHABET.find(i) - 3) % len(ALPHABET)]
    return e

def main():
    x = int(input("Entrer 0 pour chiffrer et 1 pour déchiffrer : "))
    if x == 0:
        texte = input("Entrer le texte à chiffrer : ")
        print('Après chiffrement, le texte est : ', chiffrer(texte))
    elif x == 1:
        texte = input("Entrer le texte à déchiffrer : ")
        print('Après déchiffrement, le texte est : ', dechiffrer(texte))
    else:
        print("Erreur : veuillez entrer 0 ou 1.")

if __name__ == "__main__":
    main()
