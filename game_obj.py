import random


class Card:
    def __init__(self, suit, val, hidden=0):
        self.suit = suit
        self.val = val
        self.hidden = hidden

    def close(self):
        self.hidden = 0

    def open(self):
        self.hidden = 1

class Deck:
    def __init__(self):
        self.cards = []

    def create_deck(self):
        for p in [ "spades", "hearts", "diamond", "clubs" ]:
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
        for i in range(len(self.cards) - 1):
            if ((self.cards[i].suit == suit)
            and (self.cards[i].val == val)):
                del self.cards[i]
        
    def get_index(self, suit, val) -> int:
        for i in range(len(self.cards)):
            if ((self.cards[i].suit == suit)
            and (self.cards[i].val == val)):
                return i

    def get_card(self, suit, val) -> Card:
        for i in range(len(self.cards)):
            if ((self.cards[i].suit == suit)
            and (self.cards[i].val == val)):
                return self.cards[i]

