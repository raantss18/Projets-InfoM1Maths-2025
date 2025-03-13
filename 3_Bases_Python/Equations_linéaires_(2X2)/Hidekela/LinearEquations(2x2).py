"""
    LinearEquations(2x2).py

    Author: Hidekela (MAFI)

    Description: A program resolving linear equations system with two undetermined variables

    Requirement: For visualizing the lines equations, we need matplotlib

"""

import matplotlib.pyplot as plt

class LinearEquationsSystem2x2:
    """
        Class defining a linear equations system (2 x 2)

    """

    def __init__(self, a1, b1, c1, a2, b2, c2):
        self.a1 = a1
        self.b1 = b1
        self.c1 = c1
        self.a2 = a2
        self.b2 = b2
        self.c2 = c2

        self.determinant = a1 * b2 - a2 * b1

    def is_resolvable(self):
        return self.determinant != 0

    def resolve(self):
        if not self.is_resolvable():
            return set()
            
        a1, a2, b1, b2 = self.a1, self.a2, self.b1, self.b2
        c1, c2 = self.c1, self.c2
        delta = self.determinant

        x = (b2 * c1 - b1 * c2) / delta
        y = (-a2 * c1 + a1 * c2) /delta

        return {(x, y)}

def __get_coefficient():
    a1 = float(input("Entrer a1: "))
    b1 = float(input("Entrer b1: "))
    c1 = float(input("Entrer c1: "))
    a2 = float(input("Entrer a2: "))
    b2 = float(input("Entrer b2: "))
    c2 = float(input("Entrer c2: "))

    return (a1, b1, c1, a2, b2, c2)

def showGraph(S):
    x = [_ for _ in S][0][0]

    x1 = [x - 1, x + 1]
    y1 = [(c1 - a1 * x) / b1 for x in x1]
    y2 = y1
    x2 = [(c2 - b2 * y) / a2 for y in y2]

    plt.plot(x1, y1)
    plt.plot(x2, y2)
    plt.title("Représentation des deux équations")
    plt.show()

if __name__ == "__main__":
    print("-------------------------------------------------------------------------------")
    print("------ Résolveur de système de deux équations linéaires à deux inconnues ------")
    print("-------------------------------------------------------------------------------")
    print("")

    print("L'équation est de la forme:")
    print("\ta1(x) + b1(y) = c1")
    print("\ta2(x) + b2(y) = c2")
    print("")

    a1, b1, c1, a2, b2, c2 = __get_coefficient()

    print("")
    print("On a le système :")
    print("\t", a1, "(x) +", b1, "(y) =", c1)
    print("\t", a2, "(x) +", b2, "(y) =", c2)
    print("")

    LES = LinearEquationsSystem2x2(a1, b1, c1, a2, b2, c2)
    S = set()

    if not LES.is_resolvable():
        print("Le système n'a pas de solution")
    else:
        S = LES.resolve()
        print("La solution pour ce système est {(x, y)} =", S)

        showGraph(S)
