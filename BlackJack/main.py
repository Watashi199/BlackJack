import random
from customtkinter import *
from PIL import Image

#Array des paquets de cartes
paquet = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
#Carte en main du joueur
main_joueur = []
#Carte en main du croupier
main_croupier = []

choixjoueur = ""

JOUEUR = "Joueur"
CROUPIER = "Croupier"

#Fonction pour afficher une main donnée
def print_main(main,qui):
    print("La main du", qui,":", *main)

#Fonction pour faire la somme d'une main donnée
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

#Fonction pour une tirer une carte dans la main donnée
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
    main.append(carte_tire)
    somme_cartes(main,qui)

#Fonction demandant un choix au joueur pour avancer dans la partie
def choix():
    choixjoueur = input("Que veux tu faire ?\nTu peux Tirer, Passe, FF\n")
    if choixjoueur == "Tirer":
        tirer_carte(main_joueur, joueur)
        print_main(main_joueur,joueur)
        ia_croupier()
    elif choixjoueur == "FF":
        print("A+ en LAN\n")
        exit()
    elif choixjoueur == "Passe":
        ia_croupier()

#Fonction pour gérer les choix du croupier
def ia_croupier():
    i = random.randint(1,10)
    if i <= 6:
        tirer_carte(main_croupier, croupier)
        print_main(main_croupier, croupier)
        #choix()
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

#debut_partie()

#GUI

def dp_button_callback():
    debut_partie()

def t_button_callback():
    tirer_carte(main_joueur,joueur)
    print_main(main_joueur,joueur)
    ia_croupier()

def p_button_callback():
    ia_croupier()

def f_button_callback():
    print("A+ en LAN\n")
    exit()

app = CTk()
app.title("Blackjack")
app.geometry("500x300")

text = CTkLabel(master=app, text="BLACKJACK")
text.pack(padx=0, pady=10)

action_frame = CTkFrame(master=app, fg_color="#3d85c6")
action_frame.pack(expand=True)

dp_button = CTkButton(master=app,text="Début de partie", fg_color="black", text_color="white",command=dp_button_callback)
dp_button.pack(padx=10, pady=10)

t_button = CTkButton(master=action_frame, text="Tirer", command=t_button_callback)
t_button.pack(padx=10, pady=10)

p_button = CTkButton(master=action_frame, text="Passer", command=p_button_callback)
p_button.pack(padx=0, pady=0)

f_button = CTkButton(master=action_frame, text="Fold", command=f_button_callback)
f_button.pack(padx=10, pady=10)

app.mainloop()