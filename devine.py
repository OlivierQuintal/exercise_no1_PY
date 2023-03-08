# Deviner in nombre de 1 a 10 mémorisé par l'ordinateur
import random
nombre = int(input("Entrer un nombre: de 1 a 10: "))
nombreOrdinateur = random.randint(1, 10)
nombreTrouve = False

while(nombreTrouve == False):
    if(nombre == nombreOrdinateur):
        print("Bravo vous avez trouvé le nombre")
        nombreTrouve = True
    else:
        print("Désolé vous n'avez pas trouvé le nombre")
        nombre = int(input("Entrer un nombre: de 1 a 10: "))


