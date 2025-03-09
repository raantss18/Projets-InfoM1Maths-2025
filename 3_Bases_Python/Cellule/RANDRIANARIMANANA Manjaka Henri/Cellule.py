def rule_30(left, center, right):
    """Applique la Règle 30"""
    if (left, center, right) in [(1,1,1), (1,1,0), (1,0,1), (0,0,0)]:
        return 0
    return 1

def next_generation(state):
    """Calcule la génération suivante"""
    n = len(state)
    new_state = [0] * n
    for i in range(n):
        left = state[(i-1) % n]
        center = state[i]
        right = state[(i+1) % n]
        new_state[i] = rule_30(left, center, right)
    return new_state

# Programme principal avec entrée utilisateur
if __name__ == "__main__":
    # Demander à l'utilisateur le nombre de cellules
    while True:
        try:
            width = int(input("Entrez le nombre de cellules : "))
            if width > 0:
                break
            print("Veuillez entrer un nombre positif !")
        except ValueError:
            print("Veuillez entrer un nombre valide !")
    
    # Demander le nombre de générations
    while True:
        try:
            generations = int(input("Entrez le nombre de générations : "))
            if generations > 0:
                break
            print("Veuillez entrer un nombre positif !")
        except ValueError:
            print("Veuillez entrer un nombre valide !")
    
    # Initialiser la grille avec une cellule au centre
    state = [0] * width
    state[width // 2] = 1  # Centre de la grille
    
    # Simuler et afficher
    print("\nSimulation de l'automate cellulaire (Règle 30) :")
    for _ in range(generations):
        print(''.join('█' if x else ' ' for x in state))
        state = next_generation(state)
