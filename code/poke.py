import random

def draw(deck):
    random.shuffle(deck)
    drawed_card = deck.pop()
    return drawed_card,deck

class Deck:
    def __init__(self,num_deck=20):
        self.num_deck = num_deck

    def create_deck(self):
        deck = [""]*self.num_deck
        return deck

class SarnightDeck(Deck):
    def __init__(self,num_deck=20):
        self.num_deck = num_deck

    def create_deck(self):
        if self.num_deck < 10:
            return 0
        deck = [""]*self.num_deck
        deck[:2] = ["2Draw"]*2
        deck[2:4] = ["MonBall"]*2
        deck[4:6] = ["Rartos"]*2
        deck[6:8] = ["Kiruria"]*2
        deck[8:10] = ["Sarnight"]*2
        deck[10:12] = ["Maboroshi"]*2
        deck[12:14] = ["MiuTwo"]*2
        return deck
    
def StartMatch(hands,deck):
    tmp_deck = deck
    for i in range(5):
        tmp_card,tmp_deck = draw(tmp_deck)
        hands.append(tmp_card)
    return hands,tmp_deck

hands = []
deck = SarnightDeck().create_deck()

# First Turn
hands,deck = StartMatch(hands,deck)

if "Monball" in hands :
    hands.remove("Monball")
    if "Rartos" in deck or "MiuTwo" in deck:
        

