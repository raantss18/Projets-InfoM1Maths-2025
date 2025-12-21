from os import path
from math import log10
from numpy import diff

def loadPrimes():
    if not path.exists("primes.data"):
        return []

    with open("primes.data", "r") as file:
        primes = file.read().split("\n")
    primes.pop() # remove empty

    return [int(_) for _ in primes]

def getGaps(primes):
    return diff(primes)

def getRatios(gaps, primes):
    return [gaps[i] / log10(primes[i]) for i in range(len(gaps))]

def saveGaps(gaps):
    with open("gaps.data", "w") as file:
        for gap in gaps:
            file.write(str(gap) + "\n")

def saveRatios(ratios):
    with open("ratios.data", "w") as file:
        for ratio in ratios:
            file.write(str(ratio) + "\n")

if __name__ == "__main__":
    print("Gaps and ratios of primes")
    primes = loadPrimes()

    gaps = getGaps(primes)
    saveGaps(gaps)

    ratios = getRatios(gaps, primes)
    saveRatios(ratios)

    print("Done! (see gaps.data and ratios.data)")
