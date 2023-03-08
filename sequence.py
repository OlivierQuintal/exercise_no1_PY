#5.	Faire un programme qui calcule la factorielle d’un nombre entré par l’utilisateur (par exemple, la factorielle de 5 correspond à 5 x 4 x 3 x 2 x 1) 

nombre = int(input("Entrer un nombre: "))
factorielle = 1
for i in range(1, nombre + 1):
    factorielle = factorielle * i
print("La factorielle de {0} est {1}".format(nombre, factorielle))
