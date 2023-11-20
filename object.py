import random

########
# Card #
########

pack = ["2C","3C","4C","5C","6C","7C","8C","9C","10C","JC","QC","KC","AC",
        "2S","3S","4S","5S","6S","7S","8S","9S","10S","JS","QS","KS","AS",
        "2H","3H","4H","5H","6H","7H","8H","9H","10H","JH","QH","KH","AH",
        "2D","3D","4D","5D","6D","7D","8D","9D","10D","JD","QD","KD","AD"]

# Lister les cartes présente dans le paquet
def GetListCard(pack):
    return(pack)

# Tirer une carte
def PickCard(pack):
    i = random.choice(GetListCard(pack))
    pack.remove(i)
    return(i)

##########
# Player #
##########

class Player:
    def __init__(self, name):
        self.coin = 1500
        self.handValue = 0
        self.currentCard = []
        self.name = name
        self.winnable = 1
    
    def WinCoin(self, value):
        self.coin += value

    def LooseCoin(self, value):
        self.coin -= value

    def GetCoin(self):
        return(self.coin)
    
    def DrawCard(self):
        tmp = PickCard(pack)
        if self.handValue < 21:
            self.currentCard.append(tmp)
            self.handValue += self.AppendHandValue(tmp)
        else:
            print("Tu es déjà à",self.handValue,"tu ne peux plus tirer de cartes")

    # Retourner la valeur totale de la main
    def GetHandValue(self):
        return(self.handValue)
    
    # Additionner les cartes au tirage
    def AppendHandValue(self, value):
            value = value.rstrip(value[-1])
            #Transformation des strings en int pour additionner
            match value:
                case "J":
                    value = 10
                case "Q":
                    value = 10
                case "K":
                    value = 10
                case "A":
                    value = 11
                case _:
                    value = int(value)
            return value
    
    #Définition des actions du croupier en fonction des évennement interne au jeu
    def ChoiceIA(self):
        if self.handValue < 17:
            self.DrawCard()
        elif self.handValue > 21:
                self.winnable = 1
                print("\nLe croupier est au dessus de 21 avec une main valant:",self.handValue,"\n")
        else:
            self.winnable = 0
            print("\nLe croupier passe son tour.\n")
            return(self.winnable)
    
    #Affichage les mains des joueurs
    def ShowHand(self):
        print("\nValeur de la main du",self.name,":",self.handValue,
              "\nCartes",self.name,":",' '.join(map(str, self.currentCard)),"\n")
    
    def ResetHand(self):
        self.handValue = 0
        print("New handValue",self.name, self.handValue)
        self.currentCard.clear()
        print("Main",self.name, self.handValue)

############
# Gameloop #
############

class GameLoop:
    def __init__(self):
        self.joueur = Player("Joueur")
        self.croupier = Player("Croupier")
        self.turn = 0
        self.choix = ""

    def Start(self):
        print("------------------\nDébut du jeu\n------------------\nBLACKJACK")
        self.Turn()

    def Turn(self):
        while self.turn == 0:
            print("------------------\nDébut de la manche\n------------------")
            self.DrawBoth()
            self.turn += 1  
        while self.turn >= 1:
            print("------------------------------------------------------")
            self.choix= ""
            self.ShowBoth()
            self.choix = input("A ton tour, que veux tu faire ? [T]irer une nouvelle carte, [P]asser ton tour ou te [C]oucher ?\n")
            if self.choix == "T": # Tirer
                self.DrawBoth()
                self.turn += 1
            elif self.choix == "P": # Passer
                self.croupier.ChoiceIA()
                self.turn += 1
            elif self.choix == "C": # Se coucher
                self.joueur.ResetHand()
                self.croupier.ResetHand()
                self.turn = 0
                print(self.turn)
                print("\n\n------------------\nFin de la manche\n------------------\n\n")
                self.Turn()
            else:
                print("Merci d'entrer T, P ou C")

    def ShowBoth(self):
        self.joueur.ShowHand()
        self.croupier.ShowHand()
    
    def DrawBoth(self):
        self.joueur.DrawCard()
        self.croupier.ChoiceIA()  

########
# Main #
########

gameloop = GameLoop()
gameloop.Start()