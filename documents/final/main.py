from cProfile import label
from email.mime import image
from tkinter.messagebox import OK, OKCANCEL
from tkinter.tix import COLUMN
import game_obj
import propositions
import random
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import os
import pydoc

class MyWindow:
    """
    This Class supports the development of a tkinter window.
    the __init__ function creates the fields and objects that are implemented in the window.
    im particualr a game object is created, the player decks are created for the game.
    and a single pile card is turned over. finally the main_menu method is called.
    """
    def __init__(self, win):
        self.all_rounds = {}
        self.g = game_obj.Game()
        self.g.create_player_decks()
        self.g.init_pot()
        self.win = win
        self.main_menu()

    def main_menu(self):
        """
        This method calls a button named btt1.
        the button is then placed in the tkinter window.
        clicking the button will call the function: butt3
        """
        self.btt1 = Button(self.win,
                        text="Play Yaniv",
                        command=self.butt1)
        self.btt1.grid(row=2, column=2, padx=330, pady=100)

    def butt3(self):
        """
        this method creates a new window and is run when
        the user presses the "get stats" button in the main game window.
        this new window creates a history of the game tracking all moves that have been made by
        both players.
        """
        nwin = Toplevel(self.win)
        nwin.geometry("1200x940")
        out = ""
        text = Text(nwin, height=800, width=800)
        scroll = Scrollbar(nwin)
        for rounds in self.all_rounds:
            player_1 = self.all_rounds[rounds][0]
            player_2 = self.all_rounds[rounds][1]
            pot = self.all_rounds[rounds][2]
            plyr_1prop = propositions.Propositions(player_1, pot)
            plyr_2prop = propositions.Propositions(player_2, pot)
            for card in player_1:
                out += f" {card.unicard} "
            out += f"  <--- Player 1 ({rounds}) Player 2 --->  "
            for card in player_2:
                out += f" {card.unicard} "
            out += f"    {pot[-1].unicard} "
            out += "\n"
            # out += f"Player 1\n a{plyr_1prop.a()}"
        scroll.pack(side=RIGHT)
        text.pack(side=LEFT)
        text.insert(END, out)
            

    def butt1(self):
        """
        This method acts as the
        main process in the game.
        It grabs the cards that are in the player decks, the pile deck and the game deck.
        Depending on which player's turn it is, the cards are displayed in the window, with only
        the current players cards being shown. In addition the groups are found from the get_groups method in the deck class.
        using these groups dropdown menu's are created to enable the player to make a decision on his/her move.
        all option menus are created that display all aspects of the game in the GUI window.
        """
        self.all_rounds[self.g.roundCount] = [[],[],[]]
        self.all_rounds[self.g.roundCount].append(i.unicard for i in self.g.player_decks[0].cards)
        for card in self.g.player_decks[0].cards:
            self.all_rounds[self.g.roundCount][0].append(card)
        for card in self.g.player_decks[1].cards:
            self.all_rounds[self.g.roundCount][1].append(card)
        for card in self.g.pot.cards:
            self.all_rounds[self.g.roundCount][2].append(card)
        

        if self.g.roundCount == 0:
            self.btt1.destroy()
        if ((self.g.player_decks[0].getSum() > 7) and
            (self.g.player_decks[1].getSum() > 7)):
            current_player = self.g.roundCount % 2
            if self.g.roundCount % 2 == 0:
                for card in self.g.player_decks[0].cards:
                    card.reveal()
            elif self.g.roundCount % 2 == 1:
                for card in self.g.player_decks[1].cards:
                    card.reveal()  
            self.beeone = []
            self.elone = []
            q = []
            for card in self.g.player_decks[current_player].cards:
                q.append((card.suit, card.val))   
            l1 = Label(self.win, text=f"Plyr2")
            l2 = Label(self.win, text=f"Plyr1") 
            l2.grid(row=0, column=0)
            l1.grid(row=0, column=1)
            for i in range(2):
                j = 0
                for card in self.g.player_decks[i].cards:
                    if card.hidden == 0:
                        path = 'png_96_dpi/back.png'
                    else:
                        path = card.fname
                    im = Image.open(path)
                    resized = im.resize((70, 110), Image.ANTIALIAS)
                    ph = ImageTk.PhotoImage(resized)
                    b1 = Label(self.win, image=ph)
                    self.beeone.append(b1)
                    b1.image=ph
                    b1.grid(row=j+5, column=i)
                    j+=1
            self.potl = Label(self.win, text="Pot")
            self.deckl = Label(self.win, text="Deck")
            nul = Label(self.win, text="               ")
            nul2 = Label(self.win, text="               ")
            pathhh = self.g.pot.cards[-1].fname
            pathh = 'png_96_dpi/back.png'
            imm = Image.open(pathh)
            immm = Image.open(pathhh)
            resizedd = imm.resize((70, 110), Image.ANTIALIAS)
            resizeddd = immm.resize((70, 110), Image.ANTIALIAS)
            phh = ImageTk.PhotoImage(resizedd)
            phhh = ImageTk.PhotoImage(resizeddd)
            self.deckp = Label(self.win, image=phh)
            self.deckp.image=phh
            self.potp = Label(self.win, image=phhh)
            self.potp.image=phhh
            nul.grid(row=4, column=3)
            nul2.grid(row=4, column = 0)
            self.deckl.grid(row=4, column=4)
            self.deckp.grid(row=5, column=4)
            self.potp.grid(row=6, column=4)
            self.potl.grid(row=7, column=4)
            dropdown = []
            dpdwn = ["1", "2"]
            self.g.player_decks[current_player].get_groups()
            groups1 = self.g.player_decks[current_player].groups[0]
            groups2 = self.g.player_decks[current_player].groups[1]
            if groups1:
                # group_val = []
                # diff_groups = []
                # for i in range(len(groups1)):
                #     group_val.append(groups1[i].val)
                #     if i > 0:
                #         if group_val[i] != group_val[i-1]:
                #             diff_groups.append(i)
                # s = diff_groups+[len(groups1)]  #must contain index beyond last element, alternatively use directly split_points.append(len(list1))
                # groupps2 = [groups1[i1:i2] for i1,i2 in zip([0]+s[:-1],s)]
                
                for elem in groups1:
                    sri = ""
                    for i in elem:
                        sri += f"{i.val} {i.suit};"
                    dropdown.append(sri)
                    sri=""
        
            if groups2:
                # group_val = []
                # diff_groups = []
                # for i in range(len(groups2)):
                #     group_val.append(groups2[i].val)
                #     if i > 0:
                #         if group_val[i] != group_val[i-1]:
                #             diff_groups.append(i)    
                # s = diff_groups+[len(groups2)]  #must contain index beyond last element, alternatively use directly split_points.append(len(list1))
                # groupps2 = [groups2[i1:i2] for i1,i2 in zip([0]+s[:-1],s)]
                for elem in groups2:
                    sri=""
                    for i in elem:
                        sri += f"{i.val} {i.suit};"

                    dropdown.append(sri)
                    sri=""
            print(dropdown)
            for card in self.g.player_decks[current_player].cards:
                dropdown.append(f"{card.val} {card.suit}")
            l=[]
            for i in range(len(dropdown)):
                if not dropdown[i]:
                    l.append(i)
            for index in l:
                del dropdown[index]
            self.var1 = StringVar(self.win)
            self.w = OptionMenu(self.win, self.var1, *dropdown)
            self.var2 = StringVar(self.win)
            self.w2 = OptionMenu(self.win, self.var2, *dpdwn)
            self.butttwo = Button(self.win, text="Set", command=self.butt2)
            self.buttthree = Button(self.win, text="Get Stats", command=self.butt3)
            self.dpdwnmsg = Label(self.win, text=f"        1: Replace with {self.g.pot.cards[-1].val} of {self.g.pot.cards[-1].suit} \n 2: Take up new card ")
            self.score = Label(self.win, text=
            f"{self.g.player_decks[current_player].getSum()}")
            self.dpdwnmsg.grid(row=5, column=6)
            self.w2.grid(row=6, column=6)
            self.butttwo.grid(row=8, column=6)
            self.buttthree.grid(row=10, column=6)
            dropdown = []
            self.g.player_decks[current_player].groups = [[],[]]
            if current_player == 0:
                self.w.grid(row=11, column=0)
                self.score.grid(row=10, column=0)  
            else:
                self.w.grid(row=11, column=1)
                self.score.grid(row=10, column=1) 
        else:
            newWindow = Toplevel(self.win)
            newWindow.title(f"WINNER : Player {current_player}")
            current_player = self.g.roundCount % 2

            self.deckp.destroy()
            self.potp.destroy()
            self.w.destroy()
            self.w2.destroy()
            self.score.destroy()
            self.dpdwnmsg.destroy()
            self.deckl.destroy()
            self.potl.destroy()
            self.main_menu()
            Label(newWindow, text=f"""
            Yaniv!! \n Congratulations to {current_player + 1}
            """)
            newWindow.geometry("500x270")
            

            
    def butt2(self):
        """
        this method is ran when the user presses the set button.
        it esentially acts as placing down the desired group/card and 
        picking up from either the deck or the pile.
        the groups are determined and the neccesary changes are made to the current players deck
        alongside the pile or main deck.
        """
        current_player = self.g.roundCount % 2
        ddvar1 = self.var1.get()
        ddvar2 = self.var2.get()
        cards_taken_away = [] 
        if ddvar2 == "1":
            self.g.addtoplayerDeck(current_player)
        if ddvar2 == "2":
            self.g.randomCardfromDeck(current_player)
            self.popuuCardreveal()
        s = []
        for card in self.g.player_decks[current_player].cards:
            s.append((card.suit, card.val))
        print(ddvar1)
        if ';' in ddvar1:
            split = ddvar1.split(';')
            split = split[:-1]
            for i in range(len(split)):
                slice = split[i].split(' ')
                val = slice[0]
                suit = slice[1]
                cards_taken_away.append([val, suit])
        else: 
            split = ddvar1.split()
            cards_taken_away.append([split[0], split[1]])
        
        for r in range(len(cards_taken_away)):
            val = str(cards_taken_away[r][0])
            suit = str(cards_taken_away[r][1])
            self.g.addtoPot(current_player, suit, val)
            currentcards = self.g.player_decks[current_player].cards
            for i in range(len(currentcards)):
                if str(currentcards[i].val) == val:
                    if str(currentcards[i].suit) == suit:
                        del self.g.player_decks[current_player].cards[i]
                        break

        q = []
        for card in self.g.player_decks[current_player].cards:
            q.append((card.suit, card.val))
        cards_taken_away = []
        for elem in self.beeone:
            elem.destroy()
        for elem in self.elone:
            elem.image = None
            elem.destroy()
        self.deckp.destroy()
        self.potp.destroy()
        self.w.destroy()
        self.w2.destroy()
        self.score.destroy()
        self.dpdwnmsg.destroy()
        self.deckl.destroy()
        self.potl.destroy()
        if self.g.roundCount % 2 == 0:
            for card in self.g.player_decks[0].cards:
                card.hide()
        elif self.g.roundCount % 2 == 1:
            for card in self.g.player_decks[1].cards:
                card.hide()
        self.g.roundCount += 1
        self.butt1()

    def popuuCardreveal(self):
        """
        this window is displayed when the current player
        decides to pick up a new card from the maon deck.
        it creates a new window that displayes the choice that the user made
        informing the user of the new card in their deck
        before the next player's turn.
        """
        newWindow = Toplevel(self.win)
        card = self.g.player_decks[self.g.roundCount % 2].cards[-1]
        path = card.fname
        im = Image.open(path)
        resized = im.resize((200, 270), Image.ANTIALIAS)           
        ph = ImageTk.PhotoImage(resized)
        b1 = Label(newWindow, image=ph)
        Label(newWindow, text= f""" This is the card that 
        player {self.g.roundCount%2+1} \n Just Picked Up from the deck""").grid(row=0, column=1)
        b1.image = ph
        b1.grid(row=0, column=0)
        newWindow.geometry("500x270")
        newWindow.title("Card You Picked Up:")





def main():
    """
    the main method is called to greate the
    parent window that is ultimately implemented
    by the window class. 
    """
    window=Tk()
    MyWindow(window)
    window.title('Yaniv')
    window.geometry("800x800+10+10")
    window.mainloop()

if __name__ == "__main__":
    main()
