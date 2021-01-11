mdp = input("Entrez un mot de passe (min 8 caractères) : ")
mdp_trop_court = "votre mot de passe est trop court."
if(len(mdp)==0):
    print(mdp_trop_court)
elif(len(mdp)<8 and not mdp.isdigit()):
    mdp_trop_court = mdp_trop_court.capitalize()
    print(mdp_trop_court)
elif (mdp.isdigit()):
    print("Votre mot de passe ne contient que des nombres.")
elif(mdp == "ilyaskorri"):
    print("Inscription terminée.")