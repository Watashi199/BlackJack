import random

#Array des paquets de cartes
paquet = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
#Carte en main du joueur
main_joueur = []
#Carte en main du croupier
main_croupier = []

joueur = "Joueur"
croupier = "Croupier"

def print_main(main,qui):
    print("La main du", qui,":", *main)

#Fonction pour faire la somme de la main du joueur
def somme_cartes(main, qui):
    valeur_main = 0
    #Boucle pour additionner le résultat
    for i in range(len(main)):
        valeur_main += main[i]
    #Si la main vaut plus de 21 c'est perdu gros noob
    if valeur_main > 21:
        print("Somme de la main du", qui, ":",valeur_main)
        print_main(main,qui)
        print(qui,"a perdu il a dépassé 21")
        exit()
    #Si la main vaut 21 c'est gagné
    elif valeur_main == 21:
        print("Somme de la main du", qui, ":",valeur_main)
        print_main(main,qui)
        print(qui,"a fait un BLACKJACK")
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
    print("Que veux tu faire ?")
    if input() == "Tirer":
        tirer_carte(main_joueur, joueur)
        print_main(main_joueur,joueur)
        ia_croupier()
    elif input() == "FF":
        print("Wallah j'abandonne")
        exit()
    elif input() == "Passe":
        ia_croupier()

def ia_croupier():
    i = random.randint(1,10)
    if i <= 6:
        tirer_carte(main_croupier, croupier)
        print_main(main_croupier, croupier)
        choix()
    elif i > 6:
        print("Le croupier se couche")
        print_main(main_croupier, croupier)
        exit()

#Fonction pour démarrer la partie
def debut_partie():
    tirer_carte(main_joueur, joueur)
    tirer_carte(main_joueur, joueur)
    print_main(main_joueur, joueur)
    tirer_carte(main_croupier, joueur)
    print_main(main_croupier, croupier)
    choix()

debut_partie()
