class Propositions:

    def __init__(self, deck, pot) -> None:
        self.deck = deck
        self.pot = pot

    def a(self):
        """
        checks wheter the pot card is -ge 7
        """
        if self.pot.nval >= 7:
            return True
        else:
            return False

    def b(self):
        """
        returns highest card in the deck
        """
        max_card = 0
        for card in self.deck:
            if card.nval > max_card:
                max_card = card.nval
        return card.nval

    def c(self):
        """
        there is at least one type-1 group
        """
        if self.deck.groups[0] != [[]]:
            return True
        else:
            return False


    def d(self):
        """
        there is a type-2 group
        """
        if self.deck.groups[1] != [[]]:
            return True
        else:
            return False

    def e(self):
        """
        there is a type 1 group including current pot card
        """
        for i in range(len(self.deck.cards)):
            if self.deck.cards[i].nval == self.pot.cards[-1].nval:
                return True
            else:
                return False

    def f(self):
        """
        there is a possible type 2 group including current pot card
        """
        for i in range(len(self.deck.cards)):
            if (self.deck.cards[i].suit == self.pot.cards[-1].suit):
                if (self.deck.cards[i].nval == self.pot.cards[-1].nval + 1) or (self.deck.cards[i].nval == self.pot.cards[-1].nval -1):
                    return True
                else:
                    return False
            else:
                return False

    def g(self):
        """
        there is more than one type 1 group
        """
        self.deck.get_groups()
        if len(self.deck.groups[0]) > 1:
            return True
        else:
            return False

    def h(self):
        """
        returns group with highest sum
        """
        returns = []
        self.deck.get_groups()
        if self.deck.groups != [[]]:
            current_sum = 0
            for typeGroup in self.deck.groups:
                for group in typeGroup:
                    group_sum = 0
                    for card in group:
                        group_sum+=card.nval
                    if group_sum >= current_sum:
                        current_sum = group_sum
                        for card in group:
                            returns.append(card)
        return returns

    def i(self):
        """
        there is at least one type 1 group in deck and another type 1 group including pot card 
        """
        if self.c() and self.e():
            return True
        else:
            return False

    def j(self):
        """
        there is at least one type 2 group in deck and another type 2 group including pot card
        """
        if self.d() and self.f():
            return True
        else:
            return False

    def k(self):
        """
        there are two type one groups including pot, and two type two groups including pot 
        """
        if self.i() and self.j():
            return True
        else:
            return False

    def l(self):
        """
        i is true and the greatest sum comes from group not including pot
        """
        if (self.i()) and (any(self.h() in p for p in self.deck.groups[0])):
            return True

        else:
            return False

    def m(self):
        """
        j is true and the greatest sum comes from group not including pot
        """
        if (self.j()) and (any(self.h() in p for p in self.deck.groups[1])):
            return True

        else:
            return False

    

    
        







