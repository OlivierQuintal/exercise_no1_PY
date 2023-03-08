#12.Demander à l’utilisateur d’entrer des mots, continuer tant qu’il n’entre pas une ligne vide ([Enter] sans rien écrire). Ensuite faire une chaîne de caractère avec ces mots 
mot = input("Entrer un mot:")
listeMots = []
while mot != "":
    listeMots.append(mot)
    mot = input("Entrer un autre mot ( ENTER POUR SORTIR): ")
    print(mot)
    

for i in range(len(listeMots)):
    print(mot,listeMots[i], end="")