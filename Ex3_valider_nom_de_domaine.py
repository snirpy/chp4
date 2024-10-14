continuer = True

while continuer :
    valide = True
    domaine = input("Veuilles saisir le nom de domaine: ")
    if "." not in domaine:
        print("Un nom de domaine doit contenir au moins un point!")
        continue

    parties = domaine.split(".")
    for partie in parties:
        if not partie.isalnum():
            print("Un nom de domaine ne doit pas contenir des caractères spéciaux!")
            valide = False
            break
        if not 2 <= len(parties[-1]) <= 6:
            # print(parties[-1])
            valide = False
            print("La longeur de l'extension doit être comprise entre 2 et 6")
            break
  

    if valide:
        continuer = False

if valide:
    print(f"Le nom de maine '{domaine}' est valide")
