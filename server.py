import sys
import thread
from random import shuffle
import Tkinter as tk
import socket
import nacl.secret
import nacl.utils
from nacl.hash import blake2b
import ttk


class Card:
    SUITS = ['S', 'H', 'D', 'C']
    RANKS = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    SUITS_PRINTABLE = [' - spades', ' - hearts', ' - diamonds', ' - clubs']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return self.rank + self.printable_suit(self.suit)

    def printable_suit(self, suit):
        return Card.SUITS_PRINTABLE[Card.SUITS.index(suit)]

    def greaterThan(self, card):
        return Card.RANKS.index(self.rank) > Card.RANKS.index(card.rank)

    def sameRank(self, card):
        return self.rank == card.rank


class Deck:
    SUITS = ['S', 'H', 'D', 'C']
    RANKS = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.cards = list()
        for s in Deck.SUITS:
            for r in Deck.RANKS:
                self.cards.append(Card(s, r))
        shuffle(self.cards)
        print self.cards

    def isEmpty(self):
        return len(self.cards) == 0;

    def drawCards(self, number):
        ret = list()
        for i in range(0, number):
            if len(self.cards) > 0:
                drawnCard = self.cards.pop(0)
                # print "\t\tDrawn from deck", drawnCard
                ret.append(drawnCard)
        return ret


class Game:
    def __init__(self):
        self.NUM_OF_CARDS = 6
        self.cards = [-1, -1]
        self.score = [0, 0, 0]

    def who_wins(self):
        self.score[2] += 1
        top.opp_card.set(connection.m)
        top.your_card.set(top.pick_card)
        if self.cards[0] > self.cards[1]:
            top.msg.set('You WIN!')
            self.score[0] += 1
        elif self.cards[0] < self.cards[1]:
            top.msg.set('You LOSE...')
            self.score[1] += 1
        else:
            top.msg.set('DRAW')
        self.cards[1] = -1
        self.cards[0] = -1
        top.your_s.set(self.score[0])
        top.opp_s.set(self.score[1])
        if self.score[2] == self.NUM_OF_CARDS:
            if self.score[1] < self.score[0]:
                top.msg.set('GAME OVER, You Winner!!')
            elif self.score[1] > self.score[0]:
                top.msg.set('GAME OVER, You Lose, Try Again!!')
            else:
                top.msg.set('GAME OVER, Draw, Try Again')


class Connection:
    def __init__(self, type=None):
        self.key = blake2b('password', digest_size=16)
        print len(self.key)
        self.box = nacl.secret.SecretBox(self.key)
        thread.start_new_thread(self.start, (type,))

    def start(self, type=None):
        self.s = socket.socket()  # Create a socket object
        port = 12345  # Reserve a port for your service.
        host = socket.gethostbyname(socket.gethostname())

        if type == 'server':
            self.s.bind((host, port))
            self.s.listen(1)
            self.conn, addr = self.s.accept()
            print('Got connection from', addr)
        else:
            self.s.connect((host, port))
            self.conn = self.s
        thread.start_new_thread(self.recv, ())

    def recv(self):
        # global m
        while True:
            self.m = self.dec(self.conn.recv(1024))
            if self.m:
                print(self.m)
                top.opp_card.set('********')
                game.cards[1] = Card.RANKS.index(self.m[:2].strip())

                if game.cards[0] != -1:
                    game.who_wins()

    def enc(self, msg):
        self.enc_msg = self.box.encrypt(msg)
        return self.enc_msg

    def dec(self, enc_msg):
        return self.box.decrypt(enc_msg)


class Toplevel1:
    def __init__(self, top=None):
        # global opp_card, your_card, msg, your_s, opp_s, lst_cards, y_c
        self.opp_card = tk.StringVar()
        self.opp_card.set('---')

        self.your_card = tk.StringVar()
        self.your_card.set('---')

        self.msg = tk.StringVar()
        self.msg.set('---')

        self.your_s = tk.StringVar()
        self.your_s.set('0')

        self.opp_s = tk.StringVar()
        self.opp_s.set('0')

        self.lst_cards = tk.StringVar()
        deck = Deck()
        self.y_c = deck.drawCards(game.NUM_OF_CARDS)
        self.lst_cards.set(tuple(self.y_c))

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        top.geometry("700x650+309+220")
        top.title("Durak | Server with Encryption")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Listbox1 = tk.Listbox(top)
        self.Listbox1.place(relx=0.036, rely=0.038, relheight=0.526
                            , relwidth=0.334)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(highlightbackground="#d9d9d9")
        self.Listbox1.configure(highlightcolor="black")
        self.Listbox1.configure(selectbackground="#c4c4c4")
        self.Listbox1.configure(selectforeground="black")
        self.Listbox1.configure(width=234)
        self.Listbox1.configure(listvariable=self.lst_cards)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.036, rely=0.6, height=74, width=237)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(command=self.pick)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Button''')

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.657, rely=0.108, height=21, width=74)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Your Card:''')
        self.Label1.configure(textvariable=self.opp_card)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.657, rely=0.054, height=21, width=94)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(textvariable=self.your_card)

        self.Label1_1 = tk.Label(top)
        self.Label1_1.place(relx=0.5, rely=0.046, height=21, width=74)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#d9d9d9")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''Your Card:''')

        self.Label1_3 = tk.Label(top)
        self.Label1_3.place(relx=0.471, rely=0.185, height=41, width=194)
        self.Label1_3.configure(activebackground="#f9f9f9")
        self.Label1_3.configure(activeforeground="black")
        self.Label1_3.configure(background="#d9d9d9")
        self.Label1_3.configure(disabledforeground="#a3a3a3")
        self.Label1_3.configure(foreground="#000000")
        self.Label1_3.configure(highlightbackground="#d9d9d9")
        self.Label1_3.configure(highlightcolor="black")
        self.Label1_3.configure(textvariable=self.msg)

        self.Label1_4 = tk.Label(top)
        self.Label1_4.place(relx=0.457, rely=0.108, height=21, width=104)
        self.Label1_4.configure(activebackground="#f9f9f9")
        self.Label1_4.configure(activeforeground="black")
        self.Label1_4.configure(background="#d9d9d9")
        self.Label1_4.configure(disabledforeground="#a3a3a3")
        self.Label1_4.configure(foreground="#000000")
        self.Label1_4.configure(highlightbackground="#d9d9d9")
        self.Label1_4.configure(highlightcolor="black")
        self.Label1_4.configure(text='''Opponent Card:''')

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.429, rely=0.615, relheight=0.315
                          , relwidth=0.493)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=345)

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.087, rely=0.098, height=41, width=114)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Your Score:''')

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.493, rely=0.098, height=41, width=94)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Label''')
        self.Label4.configure(textvariable=self.your_s)

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.058, rely=0.39, height=71, width=111)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Opponent Score:''')

        self.Label6 = tk.Label(self.Frame1)
        self.Label6.place(relx=0.493, rely=0.488, height=30, width=94)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''Label''')
        self.Label6.configure(textvariable=self.opp_s)

    def pick(self):
        if game.cards[0] != -1:
            return
        self.pick_card = self.Listbox1.get(tk.ACTIVE)
        game.cards[0] = Card.RANKS.index(self.pick_card[:2].strip())
        print(self.pick_card)
        self.your_card.set(self.pick_card)
        for card in self.y_c:
            if str(card) == self.pick_card:
                self.y_c.remove(card)
                break
        self.lst_cards.set(tuple(self.y_c))
        connection.conn.send(connection.enc(str.encode(self.pick_card)))

        if game.cards[1] != -1:
            game.who_wins()


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global root, top, game, connection
    root = tk.Tk()
    game = Game()
    connection = Connection('server')
    top = Toplevel1(root)
    # set_Tk_var()
    root.mainloop()


if __name__ == '__main__':
    vp_start_gui()
