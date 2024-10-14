ip = input("Entrez une adresse IP : ")

# Vérification de la présence de trois points
if ip.count('.') != 3:
    print("Adresse IP invalide : le format doit contenir 4 octets séparés par des points.")
else:
    valide = True
    octets = ip.split('.')
    
    for octet in octets:
        if not octet.isdigit() or not (0 <= int(octet) <= 255):
            print(f"Octet non valide trouvé : {octet}")
            valide = False
            break
    
    if valide:
        print("Adresse IP valide.")
