import matplotlib.pyplot as plt
from os import path
import numpy as np

from scipy.stats import expon

def loadRatios():
    if not path.exists("ratios.data"):
        return []

    with open("ratios.data", "r") as file:
        ratios = file.read().split("\n")
    ratios.pop() # remove empty

    return np.array([float(_) for _ in ratios])

def conjecturePlot(ratios):
    plt.hist(ratios, bins=100, density=True, label="Ratio $\\frac{g_k}{log(p_k)}$")
    plt.title("Distribution des écarts normalisés entre les nombres premiers")
    plt.xlabel("$\\frac{g_k}{log(p_k)}$")
    plt.ylabel("Densité")

    x = np.linspace(0, max(ratios), 500)
    plt.plot(x, expon.pdf(x, scale = 1), "r-", lw=2, label="Loi exponentielle $(\\lambda = 1)$")

    plt.legend()

    plt.show()

if __name__ == "__main__":
    print("Conjecturing")
    ratios = loadRatios()
    assert len(ratios) > 0

    print("Plotting conjecture...")
    conjecturePlot(ratios)
