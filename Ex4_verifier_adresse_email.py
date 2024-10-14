email = input("Entrez une adresse email : ")

# Vérifier qu'il y a exactement un symbole '@'
if email.count('@') != 1:
    print("Adresse email invalide : Il doit y avoir un seul '@'.")
else:
    # Séparer l'adresse en deux parties : avant et après le '@'
    partie_locale, domaine = email.split('@')

    # Vérifier que la partie locale et le domaine ne sont pas vides
    if not partie_locale or not domaine:
        print("Adresse email invalide : La partie locale ou le domaine est vide.")
    # Vérifier qu'il y a au moins un point dans le domaine et qu'il n'est ni au début ni à la fin
    elif '.' not in domaine or domaine.startswith('.') or domaine.endswith('.'):
        print("Adresse email invalide : Le domaine doit contenir un point valide.")
    else:
        # Vérifier que l'extension (après le dernier point) a au moins 2 caractères
        extension = domaine.split('.')[-1]
        if len(extension) < 2:
            print("Adresse email invalide : L'extension doit avoir au moins 2 caractères.")
        else:
            print("Adresse email valide.")
