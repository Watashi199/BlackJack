import random

#Array des paquets de cartes
paquet = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
#Carte en main du joueur
main_joueur = []
#Carte en main du croupier
main_croupier = []

joueur = "Joueur"
croupier = "Croupier"

#Fonction pour faire la somme de la main du joueur
def somme_cartes(main, qui):
    valeur_main = 0
    #Boucle pour additionner le résultat
    for i in range(len(main)):
        valeur_main += main[i]
    #Si la main vaut plus de 21 c'est perdu gros noob
    if valeur_main > 21:
        print("Somme de la main",valeur_main)
        print(main)
        print("\n",qui,"a perdu il a dépassé 21")
        exit()
    #Si la main vaut 21 c'est gagné
    elif valeur_main == 21:
        print("Somme de la main",valeur_main)
        print(main)
        print("\n",qui,"a fait un BLACKJACK")
        exit()

def tirer_carte(main,qui):
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
    main.append(carte_tire)
    somme_cartes(main,qui)

def choix():
    print("Que veux tu faire ?\n")
    if somme_cartes(main_joueur, joueur) == 21:
        print("Ta main",main_joueur[0],",", main_joueur[1])
        print("BLACKJACK")
        exit()
    elif input() == "Tirer":
        tirer_carte(main_joueur, joueur)
        print("Ta main",main_joueur[0],",", main_joueur[1],",",main_joueur[2])
    elif input() == "FF":
        print("Wallah j'abandonne")
        exit()
    elif input() == "Passe":
        return

#Fonction pour démarrer la partie
def debut_partie():
    tirer_carte(main_joueur, joueur)
    tirer_carte(main_joueur, joueur)
    print("Ta main",main_joueur[0],",", main_joueur[1])
    tirer_carte(main_croupier, joueur)
    print("Main du croupier",main_croupier[0],"\n")
    choix()

debut_partie()
