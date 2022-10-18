import random

#Array des paquets de cartes
paquet = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
#Carte en main du joueur
main_joueur = []
#Carte en main du croupier
main_croupier = []

#Fonction pour faire la somme de la main du joueur
def somme_cartes_joueur():
    valeur_joueur = 0
    #Boucle pour additionner le résultat
    for i in range(len(main_joueur)):
        valeur_joueur += main_joueur[i]
    #Si la main vaut plus de 21 c'est perdu gros noob
    if valeur_joueur > 21:
        print("Perdu tu as dépassé 21")
        exit()
    elif valeur_joueur == 21:
        print(main_joueur)
        print("BLACKJACK")
        exit()
        
def somme_cartes_croupier():
    valeur_croupier = 0
    #Boucle pour additionner le résultat
    for i in range(len(main_croupier)):
        valeur_croupier += main_croupier[i]
    #Si la main vaut plus de 21 c'est perdu gros noob
    if valeur_croupier > 21:
        print("Gagné le croupier a dépassé 21")
        exit()
    elif valeur_croupier == 21:
        print(main_croupier)
        print("Le croupier gagne !")
        exit()

#Fonction pour distribuer une carte au joueur
def tirer_carte_joueur():
    carte_tire = random.choice(paquet)
    #Transformation des strings en int pour additionner
    match carte_tire:
        case "J":
            carte_tire = 10
        case "Q":
            carte_tire = 10
        case "K":
            carte_tire = 10
        case "A":
            carte_tire = 11
        case _:
            carte_tire = int(carte_tire)
    #Ajout de la carte  a la main du joueur 
    main_joueur.append(carte_tire)
    somme_cartes_joueur()
    
#Fonction pour distribuer une carte au croupier    
def tirer_carte_croupier():
    carte_tire = random.choice(paquet)
    #Transformation des strings en int pour additionner
    match carte_tire:
        case "J":
            carte_tire = 10
        case "Q":
            carte_tire = 10
        case "K":
            carte_tire = 10
        case "A":
            carte_tire = 11
        case _:
            carte_tire = int(carte_tire)
    #Ajout de la carte  a la main du croupier 
    main_croupier.append(carte_tire)
    somme_cartes_croupier()

def choix():
    print("Que veux tu faire ?")
    if somme_cartes_joueur == 21:
        print("Ta main",main_joueur[0],",", main_joueur[1])
        print("BLACKJACK")
        exit()
    elif input() == "Tirer":
        tirer_carte_joueur()
        print("Ta main",main_joueur[0],",", main_joueur[1],",",main_joueur[2])
    elif input() == "FF":
        exit()
    elif input() == "Passe":
        return
    else:
        choix()

#Fonction pour démarrer la partie
def debut_partie():
    tirer_carte_joueur()
    tirer_carte_joueur()
    print("Ta main",main_joueur[0],",", main_joueur[1])
    tirer_carte_croupier()
    print("Main du croupier",main_croupier[0])
    choix()

debut_partie()
