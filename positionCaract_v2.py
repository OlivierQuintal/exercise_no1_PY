#Donner la position de toutes les occurrences d’un caractère dans une phrase 

charactere = input("Entrer un caractère: ")
phrase = input("Entrer une phrase: ")

nombreFois = 0

if charactere in phrase:
    for i in range(len(phrase)):
        if charactere == phrase[i]:
            nombreFois += 1
    print ("le caractère {0} est présent {1} fois dans la phrase {2}".format(charactere, nombreFois, phrase))      
else:
    print("Le caractère {0} n'est pas présent dans la phrase {1}".format(charactere, phrase))