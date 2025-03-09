import numpy as np
import math
n=int(input("Tapez n:"))
f=1
s=1
for i in range(1,n+1):
    f=f*i #calcul factoriel
    s=s+(1/f) #somme de (1/k!) pour k varie de 0 à n
    
print(s)
print("On a une marge d'erreur de ",np.fabs(s-math.e))