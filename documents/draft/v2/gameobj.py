from logging import exception
import random

class Card:
    def __init__(self, suit, val, hidden=0):
        self.suit = suit
        self.val = val
        self.hidden = hidden
        file_name = f"png_96_dpi/{suit}_{val}.png"
        self.fname = file_name
        if val == "ace":
            self.nval = 1
        elif val == "jack":
            self.nval = 11
        elif val == "queen":
            self.nval = 12
        elif val == "king":
            self.nval = 13
        else:
            self.nval = int(val)
        
        if type(self.val) == str:
            self.unicard = f"{str(self.val)[0].upper()}{self.suit[0]}"
        elif self.val == 10:
            self.unicard = f"T{self.suit[0]}"
        else:
            self.unicard = f"{str(self.val)[0]}{self.suit[0]}"

    def hide(self):
        self.hidden = 0

    def reveal(self):
        self.hidden = 1
    
    def fname(self) -> str:
        return self.fname
    
    def suit(self):
        return self.suit

    def val(self):
        return self.val

class Deck:
    def __init__(self):
        self.cards = []
        self.groups = [[], []]

    def create_deck(self):
        for p in [ "spades", "hearts", "diamonds", "clubs" ]:
            for r in range(1,14):
                if r == 1:
                    card = Card(p, "ace")
                    self.cards.append(card)
                elif r == 11:
                    card = Card(p, "jack")
                    self.cards.append(card)
                elif r == 12:
                    card = Card(p, "queen")
                    self.cards.append(card)
                elif r == 13:
                    card = Card(p, "king")
                    self.cards.append(card)
                else:
                    card = Card(p, r)
                    self.cards.append(card)

    def remove_card(self, suit, val):
        a = range(len(self.cards) -1)
        for i in a:
            if ((str(self.cards[i].suit) == str(suit))
            and (str(self.cards[i].val) == str(val))):
                del self.cards[i]

        
    def get_index(self, suit, val) -> int:
        for i in range(len(self.cards)):
            if ((str(self.cards[i].suit) == str(suit))
            and (str(self.cards[i].val) == str(val))):
                return i

    def get_card(self, suit, val):
        for i in range(len(self.cards)):
            if ((str(self.cards[i].suit) == str(suit))
            and (str(self.cards[i].val) == str(val))):
                return self.cards[i]
            else:
                return None

    def exists_already(self, c):
        for i in range(len(self.cards)):
            if ( (str(self.cards[i].suit) == str(c.suit))
            and (str(self.cards[i].suit) == str(c.suit))):
                return True
            else:
                return False
                
    def add_card(self, suit, val):
        if self.get_card(suit, val) == None:
            self.cards.append(Card(suit, val))
        else:
            raise exception()
    
    def get_groups(self):
        used_indeces = []
        for i in range(len(self.cards)):
            for j in range(len(self.cards)):
                if i < j:
                    if (self.cards[i].suit == self.cards[j].suit):
                        if self.cards[i].nval == self.cards[j].nval:
                            if i not in used_indeces:
                                used_indeces.append(i)
                                self.groups[0].append(self.cards[i])
                            if j not in used_indeces:
                                used_indeces.append(j)
                                self.groups[0].append(self.cards[j])

                    if (self.cards[i].nval == self.cards[j].nval):
                            if i not in used_indeces:
                                used_indeces.append(i)
                                self.groups[1].append(self.cards[i])
                            if j not in used_indeces:
                                used_indeces.append(j)
                                self.groups[1].append(self.cards[j])
    def getSum(self):
        suM = 0
        for card in self.cards:
            suM += card.nval
        return suM

    def getSize(self):
        return len(self.cards)
            
                
                            

class Game:
    def __init__(self, num_player=2, deck=Deck(), pot=Deck()):
        self.deck = deck
        self.pot = pot
        self.num_player = num_player
        self.player_decks = []
        self.roundCount = 0

    def create_player_decks(self):
        i = 0
        self.deck.create_deck()
        while i < self.num_player:
            plyr_deck = Deck()
            count = 0
            while count < 5:
                random_card_index = random.randint(0, len(self.deck.cards) - 1)
                suit = self.deck.cards[random_card_index].suit
                val = self.deck.cards[random_card_index].val
                plyr_deck.cards.append(self.deck.cards[random_card_index])
                self.deck.remove_card(suit, val)
                count += 1
            self.player_decks.append(plyr_deck)
            i += 1

    def init_pot(self):
        random_card_index = random.randint(0, len(self.deck.cards) - 1)
        suit = self.deck.cards[random_card_index].suit
        val = self.deck.cards[random_card_index].val
        self.pot.cards.append(self.deck.cards[random_card_index])
        self.deck.remove_card(suit, val)

    def addtoPot(self, player, suit, val):
        card = Card(suit, val)
        suit = card.suit
        val = card.val
        self.pot.cards.append(card)

    def addtoplayerDeck(self, player):
        card = self.pot.cards[-1]
        suit = card.suit
        val = card.val
        self.pot.remove_card(suit, val)
        self.player_decks[player].cards.append(card)

    def randomCardfromDeck(self, player):
        random_card_index = random.randint(0, len(self.deck.cards) - 1)
        suit = self.deck.cards[random_card_index].suit
        val = self.deck.cards[random_card_index].val
        self.deck.remove_card(suit, val)
        self.player_decks[player].add_card(suit, val)

    def removee_card(self, usr, suit, val):
        plyr_deck = self.player_decks[usr].cards
        for elem in plyr_deck:
            if elem.suit == suit:
                if elem.val == val:
                    del elem
