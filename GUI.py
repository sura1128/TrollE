#GUI

from Controller import Controller
c = Controller({})
c.setup()

prodList = c.get_product_map()

from Tkinter import *
import Tkinter
import tkMessageBox
top = Tkinter.Tk()


top.minsize(width=666, height=666)

def searchBox():
    frame = Frame(top, height=20, width=20)
    Grid.rowconfigure(top, 0, weight=1)
    Grid.columnconfigure(top, 0, weight=1)
    frame.grid(row=0, column=0, sticky=N+S+E+W)
    grid = Frame(frame, height=20, width=20)

    grid.grid(sticky=N+S+E+W, column=0, row=10, columnspan=2)
    Grid.rowconfigure(frame, 10, weight=1)
    Grid.columnconfigure(top, 0, weight=1)
    
    keyset = prodList.keys()

    for x in range(10):
        for y in range (5):
            btn = Button(frame)
            btn.grid(column=x, row=y, sticky=N+S+E+W)

    for x in range(10):
        Grid.columnconfigure(top, x, weight=1)

    for y in range(5):
        Grid.rowconfigure(top, y, weight=1)
        
        
    
w = Tkinter.Button (top, width = 50, height = 10, text = "Show Products!", command = searchBox)

w.pack()
top.mainloop()
