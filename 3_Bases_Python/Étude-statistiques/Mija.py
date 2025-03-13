import statistics as stat
import math
import random
import matplotlib.pyplot as plt
import pandas
import statsmodels.api as smi

#Une fonction qui génère deux listes de données corrélées
def gener(n):
    x=[]
    y=[]
    k=0
    for _ in range(0,100):
        x.append(random.gauss(0,1))
        y.append(random.randint(-10,10)*x[k]+random.uniform(-4,4))
        k=k+1
    return (x,y)

#Une fonction qui étudie les propriétés statistiques d'une liste
def statistika(x):
    medi=stat.median(x)
    mode=stat.mode(x)
    espe=stat.mean(x)
    vari=stat.variance(x)
    ectp=stat.stdev(x)
    return (medi,mode,espe,vari,ectp)

#la fonction main
n=int(input("Veuillez entrer la taille des deux listes que vous vouler  :"))
x,y=gener(n)
x_medi,x_mode,x_espe,x_vari,x_ectp=statistika(x)
y_medi,y_mode,y_espe,y_vari,y_ectp=statistika(y)
liste=['médiane','mode','espérance','variance','écart-type']
liste_x=[x_medi,x_mode,x_espe,x_vari,x_ectp]
liste_y=[y_medi,y_mode,y_espe,y_vari,y_ectp]
print("La covariance des deux données vaut",stat.covariance(x,y))
print("Le coefficient de corrélation des deux données est de ", stat.correlation(x,y))
print("******Tableau récapitulatifs de quelques propriétés statistiques des deux listes de données******")
dataset=pandas.DataFrame({"Propriétés":liste,"x":liste_x,"y":liste_y})
dataset.head()
plt.title("Nuage de points")
plt.scatter(x,y,color="green")
#un tableau qui résume la regression linéaire entre les deux listes
A=smi.add_constant(x)
model=smi.OLS(x,A)
results=model.fit()
print(results.summary())
import seaborn as sns
print("******Droite de regression linéaire*****")
sns.regplot(x=x,y=y,ci=None,color="forestgreen")
liste_a=[x_espe,x_vari,x_ectp]
liste_b=[0,1,1]
lis=['espérance','variance','écart-type']
print("******Tableau comparison des valeurs théoriques et pratiques de la première liste ******")
info=pandas.DataFrame({"Propriétés":lis,"Téories":liste_b,"Réelles":liste_a})
info.head()
print("L'éspérance théorique de la deuxième liste vaut 0,sa valeur réeelle est",y_espe,".")

