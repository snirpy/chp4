machaine = input("Saisir une chaine: ")
i = 0
for element in machaine:
    
    if element.isdigit():
        print(element,end='')
        i += 1
        if i % 2 == 0:
            print("", end=" ")