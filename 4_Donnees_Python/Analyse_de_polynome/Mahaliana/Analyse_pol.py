import math
import matplotlib.pyplot as plt

def polynome(i, a, b, c):
   f = a * i**2 + b * i + c
   return f

def racine(a, b, c): #calcul des racines du polynôme
   
   if a == 0 :
      r = -c / b
      print(f"Le polynôme admet une racine r = {r}")
   else:
          delta = b**2 - 4*a*c

          if delta < 0 :
              print("Le polynôme n'admet pas de racine")

          elif delta == 0 :
               r = -b / 2*a
               print(f"Le polynôme admet une racine unique r = {r}")
          elif delta > 0 :
             r1  =  (-b + (math.sqrt(delta)))/ 2*a
             r2  =  (-b - (math.sqrt(delta)))/ 2*a
             print(f" Le polynôme admet deux racines r1 = {r1} et r2 = {r2} ")

#lire la valeur des coefficients
a = float(input("entrer la valeur de a : "))
b = float(input("entrer la valeur de b : "))
c = float(input("entrer la valeur de c : "))

print ( f" {a}x²+ {b}x + {c}") #affichage du polynôme


#générer la valeur de x
x = [ i for i in range(101) ] # 0 a 100

#valeur de f(x) pour chaque x
y = [polynome( i, a, b, c) for i in x]

plt.plot(x, y)

#titre et legende des axes
plt.title("Courbe representative du polynôme")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.show() #affichage du graphique
plt.savefig("Graphique.png") #enregistrement du graphe dans un fichier .png

racine(a , b, c)
