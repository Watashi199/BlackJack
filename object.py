import random

########
# Card #
########

class Card:
    def __init__(self):
        self.pack = ["2C","3C","4C","5C","6C","7C","8C","9C","10C","JC","QC","KC","AC",
                     "2S","3S","4S","5S","6S","7S","8S","9S","10S","JS","QS","KS","AS",
                     "2H","3H","4H","5H","6H","7H","8H","9H","10H","JH","QH","KH","AH",
                     "2D","3D","4D","5D","6D","7D","8D","9D","10D","JD","QD","KD","AD"]
        self.cardLeft = 52
        self.valueLeft = 0

    # Lister les cartes présente dans le paquet
    def GetListCard(self):
        return(self.pack)
    
    # Tirer une carte
    def DrawCard(self):
        self.cardLeft -= 1
        return random.choice(self.GetListCard())

##########
# Player #
##########

class Player:
    def __init__(self, name):
        self.coin = 1500
        self.handValue = 0
        self.currentCard = []
        self.name = name
        self.winnable = 0
    
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
    
    def GetCurrentHand(self):
        return(self.currentCard)

############
# Gameloop #
############

class GameLoop:
    def __init__(self):
        self.paquet = Card()
        self.joueur = Player("Joueur")
        self.croupier = Player("Croupier")
        self.turn = 0
        self.choix = ""

        def CheckWinCondition(self):
            if self.joueur.handValue == 21:
                print("T'as gagné toussa toussa")
            elif self.croupier.handValue == 21:
                print("Le croupier a gagné t'es nul")
            # Condition de loose instantanée
            elif self.joueur.handValue > 21:
                print("T'as dépassé 21, t'as gagné bisous")
                print("\n\n")
                print("- Fin de la partie -\n\n")
                GameLoop()
            elif self.croupier.handValue > 21:
                print("Le croupier a dépassé 21, t'as gagné bisous")
                print("\n\n")
                print("- Fin de la partie -\n\n")
                GameLoop()

            # elif self.joueur.handValue > self.croupier.handValue and self.joueur.handValue <= 21:
            #     print("Tu as battu le croupier bj")
            # elif self.croupier.handValue > self.joueur.handValue and self.croupier.handValue <= 21:
            #     print("Le croupier a gagné")

        def DrawAppendJoueur(self):
            tmp = self.paquet.DrawCard()
            self.joueur.currentCard.append(tmp)
            self.joueur.handValue += self.croupier.AppendHandValue(tmp)
            print("Valeur de la main du joueur :",self.joueur.handValue)
            print("Cartes joueur :",' '.join(map(str, self.joueur.currentCard)),"\n") 
            
        def DrawAppendCroupier(self):
            tmp = self.paquet.DrawCard()
            self.croupier.currentCard.append(tmp)
            self.croupier.handValue += self.croupier.AppendHandValue(tmp)
            print("Valeur de la main du croupier :",self.croupier.handValue)
            print("Cartes croupier :",' '.join(map(str, self.croupier.currentCard)),"\n") 

        while self.turn == 0:
            DrawAppendJoueur(self)
            DrawAppendCroupier(self)
            print("Il reste",self.paquet.cardLeft,"cartes dans le paquet\n")
            self.turn += 1

        while self.turn >= 1:
            self.choix= ""
            self.choix = input("A ton tour, que veux tu faire ? [T]irer une nouvelle carte, [P]asser ton tour ou te [C]oucher ?\n")
            if self.choix == "T": # Tirer
                DrawAppendJoueur(self)
                DrawAppendCroupier(self)
                print("Il reste",self.paquet.cardLeft,"cartes dans le paquet\n")
                self.turn += 1
                CheckWinCondition(self)
            elif self.choix == "P": # Passer
                print("Valeur de la main du joueur :",self.joueur.handValue)
                print("Cartes joueur :",' '.join(map(str, self.joueur.currentCard)),"\n") 
                DrawAppendCroupier(self)
                print("Il reste",self.paquet.cardLeft,"cartes dans le paquet\n")
                self.turn += 1
                CheckWinCondition(self)
            elif self.choix == "C": # Se coucher
                print("\n\n")
                print("- Fin de la partie -\n\n")
                GameLoop()
            else:
                print("Merci d'entrer T, P ou C")

########
# Main #
########

gameloop = GameLoop()
