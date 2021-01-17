
date=input("Veuillez entrer la date sous le format jj/mm/aa : ")
for i in range(len(date)):
    if date[i].isdigit():
        print(date[i],end ='')
    else:
        print(" ",end = '')
