from logging import exception
import random
import pydoc

class Card:
    """
    The card object contains 2 arguments:
    the suit, the value, and an integer value representing
    the cards value from 1 to 13 is created from this infromation.
    the card can ve hidden to inform the later methods that it is
    not the current players turn.
    In addition the file name containing a file name
    associated with a png is used to eventually display the card 
    """
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
    """
    the deck object constructor takes no arguments, instead creating an
    empty list to hold the card objects.
    and creating a 2D list to hold the groups of type one and two.
    there are other methods implemented within this class that apply
    the functonality of this class.
    """
    def __init__(self):
        self.cards = []
        self.groups = [[], []]

    def create_deck(self):
        """
        this method creates a standard 52 card deck and is only to be ran once per game.
        it appends these cards to the list self.cards . 
        """
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
        """
        this method removes a card of suit and val
        from the deck 
        """
        a = range(len(self.cards) -1)
        for i in a:
            if ((str(self.cards[i].suit) == str(suit))
            and (str(self.cards[i].val) == str(val))):
                del self.cards[i]

        
    def get_index(self, suit, val) -> int:
        """
        this method returns the index of a card with 
        suit and val.
        """
        for i in range(len(self.cards)):
            if ((str(self.cards[i].suit) == str(suit))
            and (str(self.cards[i].val) == str(val))):
                return i

    def get_card(self, suit, val):
        """
        this method returns the card with 
        suit and val. (useful when specific memory 
        address requiresd)
        """
        for i in range(len(self.cards)):
            if ((str(self.cards[i].suit) == str(suit))
            and (str(self.cards[i].val) == str(val))):
                return self.cards[i]
            else:
                return None

    def exists_already(self, c):
        """
        returns a boolean regarding the existence of
        a card c within the deck. verifying correct
        memory adress.
        """
        for i in range(len(self.cards)):
            if ( (str(self.cards[i].suit) == str(c.suit))
            and (str(self.cards[i].suit) == str(c.suit))):
                return True
            else:
                return False
                
    def add_card(self, suit, val):
        """
        this method adds a card with suit and val
        to the deck. 
        """
        if self.get_card(suit, val) == None:
            self.cards.append(Card(suit, val))
        else:
            raise exception()
    
    def get_groups(self):
        """
        this method returns the groups of the deck.
        it checks for both type 1 and 2 groups.
        placing each set of groups within the list to be returned.
        """
        used_indeces1 = []
        used_indeces2 = []
        lastAppendedCard=Card("invalid", "999")
        group = []
        group2 = []
        for i in range(len(self.cards)):
            for j in range(len(self.cards)):
                if i < j:
                    if (self.cards[i].suit == self.cards[j].suit):
                        if (self.cards[i].nval == self.cards[j].nval + 1) or (self.cards[i].nval == self.cards[j].nval -1):
                            if i not in used_indeces1:
                                used_indeces1.append(i)
                                group2.append(self.cards[i])
                            if j not in used_indeces1:
                                used_indeces1.append(j)
                                group2.append(self.cards[j])
                    if (self.cards[i].nval == self.cards[j].nval):
                            if self.cards[i].nval != lastAppendedCard.nval and lastAppendedCard.nval != 999:
                                if self.cards[j].nval != lastAppendedCard.nval:
                                    self.groups[0].append(group)
                                    group=[]
                            if i not in used_indeces2:
                                used_indeces2.append(i)
                                group.append(self.cards[i])
                                lastAppendedCard=self.cards[i]
                            if j not in used_indeces2:
                                used_indeces2.append(j)
                                group.append(self.cards[j])
                                lastAppendedCard=self.cards[i]
        self.groups[0].append(group)
        self.groups[1].append(group2)
        
        # for p in range(len(self.groups)):
        #     group_val = []
        #     diff_groups = []
        #     for i in range(len(self.groups[p])):
        #         group_val.append(self.groups[p][i].val)
        #         if i > 0:
        #             if group_val[i] != group_val[i-1]:
        #                 diff_groups.append(i)
        #     s = diff_groups+[len(self.groups[p])]  #must contain index beyond last element, alternatively use directly split_points.append(len(list1))
        #     self.groups[p] = [self.groups[p][i1:i2] for i1,i2 in zip([0]+s[:-1],s)]
        if len(self.groups[1][0]) < 3:
            self.groups[1] = [[]]
        
    def getSum(self):
        """
        this function returns the sum of cards in the current deck.
        """
        suM = 0
        for card in self.cards:
            suM += card.nval
        return suM

    def getSize(self):
        """
        returns the length of the list
        containg the cards in the deck.
        """
        return len(self.cards)
            
                
                            

class Game:
    """
    this class is used to hold varous objects that are used in the game,
    in particular creating various instances go deck objects to represent the 
    main deck, the player decks and the pile deck. 
    """
    def __init__(self, num_player=2, deck=Deck(), pot=Deck()):
        """
        the constructor creates the player decks list, pot deck and main deck objects.
        it also creates an integer to track the roundcount.
        """
        self.deck = deck
        self.pot = pot
        self.num_player = num_player
        self.player_decks = []
        self.roundCount = 0

    def create_player_decks(self):
        """
        this method creates the player decks by removing 10 cards from the main deck
        and allocating 5 per player. the cards are chosen at random to ensure
        proper "shuffling" is applied.
        """
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
        """
        this method initializes the pot deck by taking
        one ramdom card from the deck and placing it in the
        pot deck.
        """
        random_card_index = random.randint(0, len(self.deck.cards) - 1)
        suit = self.deck.cards[random_card_index].suit
        val = self.deck.cards[random_card_index].val
        self.pot.cards.append(self.deck.cards[random_card_index])
        self.deck.remove_card(suit, val)

    def addtoPot(self, player, suit, val):
        """
        this method adds a new card object with specific suit and value
        to the pot deck
        """
        card = Card(suit, val)
        suit = card.suit
        val = card.val
        self.pot.cards.append(card)

    def addtoplayerDeck(self, player):
        """
        given a player number (0 or 1): the
        last card placed in the pot deck is placed into
        that players deck
        """
        card = self.pot.cards[-1]
        suit = card.suit
        val = card.val
        self.pot.remove_card(suit, val)
        self.player_decks[player].cards.append(card)

    def randomCardfromDeck(self, player):
        """
        this method takes a player number and places a random card from
        the main deck into that players deck.
        """
        random_card_index = random.randint(0, len(self.deck.cards) - 1)
        suit = self.deck.cards[random_card_index].suit
        val = self.deck.cards[random_card_index].val
        self.deck.remove_card(suit, val)
        self.player_decks[player].add_card(suit, val)

    def removee_card(self, usr, suit, val):
        """
        this method removes a card with a suit and value
        from a specific players deck
        """
        plyr_deck = self.player_decks[usr].cards
        for elem in plyr_deck:
            if elem.suit == suit:
                if elem.val == val:
                    del elem