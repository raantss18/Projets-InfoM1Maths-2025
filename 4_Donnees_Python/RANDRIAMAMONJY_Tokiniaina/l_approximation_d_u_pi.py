#project_numero_4
import math
import matplotlib.pyplot as plt
import random
n=1000000

point_c=0
prg=[]
for i in range(1,n+1):
    x=random.uniform(-1, 1)
    y=random.uniform(-1, 1)
    if x**2+y**2<=1:
            point_c+=1
            pi_approx=4*(point_c)/i
            prg.append(pi_approx)
pi_approx=prg[-1]
erreur=abs(math.pi-pi_approx)
print(f"la valeur de pi est_approximé à {pi_approx} avec {erreur} d'erreur pour {n} point")
plt.plot(prg)
plt.axhline(y=math.pi, color='r', linestyle='--')
plt.title("L'évolution d'approximation de pi")
plt.xlabel("nombre_du_point")
plt.ylabel("les approximation du pi approprié à ces estimation")
plt.show()
            