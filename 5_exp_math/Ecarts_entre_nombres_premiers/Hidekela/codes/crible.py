from math import sqrt
from time import time

def cribleEratosthene(n):
    assert type(n) == int
    assert n > 1

    isPrimeList = [0, 0] + [1] * (n - 1)

    # erase the even numbers
    for multipleOf2 in range(4, n + 1, 2):
        isPrimeList[multipleOf2] = 0

    # range to sqrt(n) is enough because if m > n, we have m*m > n*n (see the next loop)
    # step = 2 because primes after 2 are odd
    for i in range(3, int(sqrt(n)) + 1, 2):
        # i*i because with n < i, i*n is already killed by n
        for multiple in range(i * i, n + 1, i):
            isPrimeList[multiple] = 0

    return [key for key, value in enumerate(isPrimeList) if value]

def cribleSegmented(n, seg_size = pow(10, 5)):
    limit = int(sqrt(n))
    smallPrimes = cribleEratosthene(limit)

    seg_size = min(seg_size, n - limit + 1)
    a, b = limit + 1, limit + seg_size

    primes = [] + smallPrimes

    while a <= n:
        isPrimesSegment = [1] * seg_size
        for p in smallPrimes:
            firstMultiple = max(p * p, ((a + p - 1) // p) * p)
            for multiple in range(firstMultiple - a, seg_size, p):
                isPrimesSegment[multiple] = 0
        primes += [key + a for key, value in enumerate(isPrimesSegment) if value]

        a = b + 1
        b = min(b + seg_size, n)
        seg_size = b - a + 1

    return primes

def __recordTimeStart():
    global t
    t = time()

def __getTimeEnd():
    global t
    return time() - t

def __saveInFile(primes):
    with open("primes.data", "w") as file:
        file.write("\n".join([str(_) for _ in primes]) + '\n')

if __name__ == "__main__":
    print("Get primes under n")
    n = int(input("Enter n: "))

    __recordTimeStart()
    primes = cribleSegmented(n)
    duration = __getTimeEnd()
    __saveInFile(primes)

    print("Here are the primes:", primes)
    print("Duration (sec):", duration)
