from durak.game import Game
from durak.bot import Bot
from durak.ui import UI

game = Game()

ai = Bot()
human = UI()

game.addPlayer(human)
game.addPlayer(ai)

game.start()

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    set_Tk_var()
    top = Toplevel1(root)
    init(root, top)
    root.mainloop()


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


def set_Tk_var():
    global lst2
    lst2 = tk.StringVar()
    global lst3
    lst3 = tk.StringVar()
    global lst1
    lst1 = tk.StringVar()
    global my_lst
    my_lst = tk.StringVar()


def pick():
    p = w.list_cards.get(tk.ACTIVE)
    print p
    w.list_cards.delete(a.index(p))


def stop():
    global a
    a = [1, 2, 3, 4, 5]
    for c in a:
        w.list_cards.insert('end', c)
    print('unknown_support.stop')
    sys.stdout.flush()


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        top.geometry("615x519+353+136")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.016, rely=0.019, relheight=0.684
                          , relwidth=0.967)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=595)

        self.list_enemy2 = tk.Listbox(self.Frame1)
        self.list_enemy2.place(relx=0.403, rely=0.028, relheight=0.287
                               , relwidth=0.192)
        self.list_enemy2.configure(background="white")
        self.list_enemy2.configure(disabledforeground="#a3a3a3")
        self.list_enemy2.configure(font="TkFixedFont")
        self.list_enemy2.configure(foreground="#000000")
        self.list_enemy2.configure(highlightbackground="#d9d9d9")
        self.list_enemy2.configure(highlightcolor="black")
        self.list_enemy2.configure(selectbackground="#c4c4c4")
        self.list_enemy2.configure(selectforeground="black")
        self.list_enemy2.configure(width=114)
        self.list_enemy2.configure(listvariable=lst2)

        self.list_enemy1 = tk.Listbox(self.Frame1)
        self.list_enemy1.place(relx=0.739, rely=0.028, relheight=0.287
                               , relwidth=0.192)
        self.list_enemy1.configure(background="white")
        self.list_enemy1.configure(disabledforeground="#a3a3a3")
        self.list_enemy1.configure(font="TkFixedFont")
        self.list_enemy1.configure(foreground="#000000")
        self.list_enemy1.configure(highlightbackground="#d9d9d9")
        self.list_enemy1.configure(highlightcolor="black")
        self.list_enemy1.configure(selectbackground="#c4c4c4")
        self.list_enemy1.configure(selectforeground="black")
        self.list_enemy1.configure(width=114)
        self.list_enemy1.configure(listvariable=lst3)

        self.list_enemy3 = tk.Listbox(self.Frame1)
        self.list_enemy3.place(relx=0.067, rely=0.028, relheight=0.287
                               , relwidth=0.192)
        self.list_enemy3.configure(background="white")
        self.list_enemy3.configure(disabledforeground="#a3a3a3")
        self.list_enemy3.configure(font="TkFixedFont")
        self.list_enemy3.configure(foreground="#000000")
        self.list_enemy3.configure(highlightbackground="#d9d9d9")
        self.list_enemy3.configure(highlightcolor="black")
        self.list_enemy3.configure(selectbackground="#c4c4c4")
        self.list_enemy3.configure(selectforeground="black")
        self.list_enemy3.configure(width=114)
        self.list_enemy3.configure(listvariable=lst1)

        self.bnt_finish = tk.Button(top)
        self.bnt_finish.place(relx=0.033, rely=0.732, height=73, width=99)
        self.bnt_finish.configure(activebackground="#ececec")
        self.bnt_finish.configure(activeforeground="#000000")
        self.bnt_finish.configure(background="#d9d9d9")
        self.bnt_finish.configure(command=stop)
        self.bnt_finish.configure(disabledforeground="#a3a3a3")
        self.bnt_finish.configure(foreground="#000000")
        self.bnt_finish.configure(highlightbackground="#d9d9d9")
        self.bnt_finish.configure(highlightcolor="black")
        self.bnt_finish.configure(pady="0")
        self.bnt_finish.configure(text='''Finished Turn''')

        self.list_cards = tk.Listbox(top)
        self.list_cards.place(relx=0.374, rely=0.732, relheight=0.139
                              , relwidth=0.267)
        self.list_cards.configure(background="white")
        self.list_cards.configure(disabledforeground="#a3a3a3")
        self.list_cards.configure(font="TkFixedFont")
        self.list_cards.configure(foreground="#000000")
        self.list_cards.configure(highlightbackground="#d9d9d9")
        self.list_cards.configure(highlightcolor="black")
        self.list_cards.configure(selectbackground="#c4c4c4")
        self.list_cards.configure(selectforeground="black")
        self.list_cards.configure(width=164)
        self.list_cards.configure(listvariable=my_lst)

        self.bnt_pick = tk.Button(top)
        self.bnt_pick.place(relx=0.813, rely=0.732, height=73, width=99)
        self.bnt_pick.configure(activebackground="#ececec")
        self.bnt_pick.configure(activeforeground="#000000")
        self.bnt_pick.configure(background="#d9d9d9")
        self.bnt_pick.configure(command=pick)
        self.bnt_pick.configure(disabledforeground="#a3a3a3")
        self.bnt_pick.configure(foreground="#000000")
        self.bnt_pick.configure(highlightbackground="#d9d9d9")
        self.bnt_pick.configure(highlightcolor="black")
        self.bnt_pick.configure(pady="0")
        self.bnt_pick.configure(text='''Pick Card''')


if __name__ == '__main__':
    vp_start_gui()
