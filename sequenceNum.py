# 	Afficher la séquence des nombres compris entre deux nombres entrés (dans n’importe quel ordre) par l’utilisateur

nombre1 = int(input("Entrer un nombre: "))
nombre2 = int(input("Entrer un deuxieme nombre: "))

if nombre1 < nombre2:
    for i in range(nombre1 +1, nombre2):
        print(i)
elif nombre1 > nombre2:
    for i in range(nombre2 +1, nombre1):
        print(i)