#8.	Rechercher si un caractère est présent dans une chaîne entrée par l’utilisateur 

charactere = input("Entrer un caractère: ")
phrase = input("Entrer une phrase: ")

if charactere in phrase:
    emplacement = phrase.find(charactere)
    print("Le caractère {0} est présent dans la phrase {1} à l'emplacement {2}".format(charactere, phrase, emplacement))
else:
    print("Le caractère {0} n'est pas présent dans la phrase {1}".format(charactere, phrase))