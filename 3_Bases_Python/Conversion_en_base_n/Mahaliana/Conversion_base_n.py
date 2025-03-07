def Conversion_base_n():
    
    n = int(input("Entrer un entier en base 10 : "))
    base = int(input("Entrer la base de conversion : "))
    
    if base < 2 or base > 16 :
        raise ValueError("La base de conversion doit être comprise entre 2 et 16 ")
    
    Symboles = "0123456789ABCDEFG" #les symboles pour bases jusqu'à 16
    Resultat = ""
    
    if n == 0 :
        Resultat = 0

    while n > 0 :
        reste = n % base #récuperation du reste
        Resultat = Symboles [reste]+ Resultat #ajout du reste en tête 
        n //= base #mise à jour du quotient
   
    print("Resultat :",Resultat)

Conversion_base_n()



 