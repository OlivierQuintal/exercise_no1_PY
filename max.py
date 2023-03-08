#Trouver la valeur maximale dans une liste d'entiers prédéfinie dans le programme 

listeNombre = [-45, 22, -34, 12, 33, 19]
max = listeNombre[0]
for nombre in listeNombre:
    if(nombre > max):
        max = nombre    
print("Le nombre le plus grand est {0}".format(max))