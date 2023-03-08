nombre = int(input("Entrez un nombre positif svp:"))

n = 2

premier = True

while n < nombre and premier :
    if ( nombre % n ) == 0 :
         premier = False
    else:
        n+=1

if premier:
    print(nombre, " est un nombre premier")
else:
    print(nombre, " n'est pas un nombre premier")
