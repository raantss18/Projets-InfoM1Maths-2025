class Polynome:
    def __init__(self, entries:list):
        #On supprime les zéros à la fin de la liste `entries`
        for i, coeff in enumerate(reversed(entries)):
            if coeff != 0: entries = entries[:len(entries)-i]; break
            elif i == len(entries) - 1: entries = [0]
        # Définir les attribus
        self.entries = entries
        self.degree = len(self.entries) - 1
    
    def __str__(self) -> str:
        """Renvoi le polynôme sous forme de chaîne de caractères"""
        P_str = f"{self.entries[0]}"
        for i, coeff in enumerate(self.entries): 
            if i == 0 or coeff == 0: continue
            else: P_str += f" {"+" if coeff > 0 else "-"} {abs(coeff) if abs(coeff) != 1 else ""}x{f"^{i}" if i != 1 else ""}"
        return P_str

    def of(self, x:float) -> float:
        """Evalue le pôlynome en x"""
        P_x = 0
        for i, coeff in enumerate(self.entries): P_x += coeff * (x**i)
        return P_x

    def __add__(self, OTHER:"Polynome") -> "Polynome":
        """Additionne deux pôlynomes"""
        P = Polynome(self.entries); Q = Polynome(OTHER.entries) # Recréer `self` et `OTHER` pour corriger les eventuelles modifications indésirables des attributs `.entries` et`.degree`
        d1 = P.degree; d2 = Q.degree; d = max(d1, d2)
        P.entries += [0]*abs(d1 - d); Q.entries += [0]*abs(d2 - d) # Completer P.entries ou Q.entries par des zéros pour qu'ils aient la même taille
        return Polynome([P.entries[i]+Q.entries[i] for i in range(d+1)])
    
    def __mul__(self, OTHER) -> "Polynome":
        """Multiplie deux polynomes ou un polynome et un scalaire """
        if type(OTHER) == Polynome: # produit de deux polynomes
            P = Polynome(self.entries); Q = Polynome(OTHER.entries) # Recréer `self` et `OTHER` comme dans `__add__`
            if P.entries == [0] or Q.entries == [0]: PRODUCT = Polynome([0]) # PRODUIT nul si P est nul ou Q est nul: pour eviter des boucles unitiles
            else:
                PRODUCT = Polynome([0])
                for i, coeff_P in enumerate(P.entries): # Faire le produit de chaque monômes de P par Q et faire et ajouter le produit à `PRODUIT`
                    if coeff_P == 0: continue 
                    else: PRODUCT += Polynome([0]*i + [(coeff_Q * coeff_P) for coeff_Q in Q.entries])
            return PRODUCT
        elif type(OTHER) in (float, int): # produit d'un polynome par un scalaire de type `P(x) * a`
            return self * Polynome([OTHER])

    def __rmul__(self, x) -> "Polynome": 
        """produit d'un polynome par un scalaire de type `a * P(x)`"""
        return self * x
    
    def __sub__(self, OTHER:"Polynome") -> "Polynome":
        """Soustraction"""
        return self + (-1)*OTHER


def test_polynome():
    import time
    print("*** POLYNOMES ***")
    x = 1; y = -2
    N = Polynome([0]); P = Polynome([1, 1]); Q = Polynome([2, -3, 0, -8, 9])
    print(f"P(x) = {P.__str__()} \n => P({x}) = {P.of(x)}")
    print(f"Q(x) = {Q.__str__()} \n => Q({y}) = {Q.of(y)}")
    print(f"N(x) = {N.__str__()}")
    S = P+Q; T = P*Q; M = N*P 
    print(f"P(x) + Q(x) = {S.__str__()}")
    print(f"P(x) * Q(x) = {T.__str__()}")
    print(f"P(x) * N(x) = {M.__str__()}")
    print(f"-2 * Q(x) = {(-2 * Q).__str__()}")

    """
    P = Polynome(range(10000))
    t_i = time.time()
    #print((P*P).__str__())
    print("Calculer Q...")
    Q = P*P
    print("Finished !")
    print(f"Execution time: {time.time() - t_i}") 

    t_i = time.time()
    print(Q.of(-2))
    print(f"Execution time: {time.time() - t_i}") 
    """
if __name__ == '__main__': 
    test_polynome()
