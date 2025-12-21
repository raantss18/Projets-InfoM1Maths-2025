import matplotlib.pyplot as plt
from os import path
import numpy as np

def loadRatios():
    if not path.exists("ratios.data"):
        return []

    with open("ratios.data", "r") as file:
        ratios = file.read().split("\n")
    ratios.pop() # remove empty

    return np.array([float(_) for _ in ratios])

def plotRatiosHistogram(ratios, E):
    plt.hist(ratios)
    plt.title("Histogramme des ratios (espérance empirique: " + str(E)  + ")")
    plt.xlabel("$k$")
    plt.ylabel("$\\frac{g_k}{log(p_k)}$")

    plt.show()

def __saveInFile(empiricExpectation):
    with open("empiricExpectation.data", "w") as file:
        file.write("Empiric expectation: " + str(empiricExpectation) + '\n')

if __name__ == "__main__":
    print("Empiric expectation:")
    ratios = loadRatios()
    assert len(ratios) > 0
    E = np.mean(ratios)
    __saveInFile(E)
    print("E =", E)

    print("Plotting ratios histogram...")
    plotRatiosHistogram(ratios, E)
