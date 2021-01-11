nom = input ("Saisir une phrase: ")
taille = len(nom)
for i in range(taille-1, -1, -1):
    print(nom[i], end='')

print("\n\n")
for lettre in reversed(nom):
    print(lettre, end='')

print("")
for lettre in nom[::-1]:
    print(lettre, end='')
