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
    print('unknown_support.pick')
    sys.stdout.flush()

def stop():
    print('unknown_support.stop')
    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import unknown
    unknown.vp_start_gui()




