#GUI

from Controller import Controller
c = Controller({})
c.setup()

prodList = c.get_product_map()

from Tkinter import *
import Tkinter
import tkMessageBox
import ttk
import tkFont

top = Tkinter.Tk()
top.minsize(width=500, height=500)
frame = Frame(top)
grid = Frame(frame)


top.configure(bg='black')
customFont = tkFont.Font(family="Cambria", size=14)
prodFont = tkFont.Font(family="Cambria", size=12)


def main_UI():
    var = StringVar()
    label = Label(top, textvariable=var, relief=RAISED, height=5, width=60, fg="white", bg="red4", anchor=CENTER, font=customFont)
    var.set("WELCOME TO TROLL-E! How can we help you today? >^^<")
    label.pack()
    w = Tkinter.Button (top, width = 40, height = 4, text = "Show Products!", command = searchBox, bg="DeepSkyBlue4", fg="white", font=customFont)
    w.pack(pady=60, padx=60, expand=True)


def hideFrame(label):
    label.pack_forget()
    frame.pack_forget()
                

def searchBox():    
    Grid.rowconfigure(top, 0, weight=1)
    Grid.columnconfigure(top, 0, weight=1)
    frame.grid(row=0, column=0,sticky=N+S+E+W)

    grid.grid(sticky=N+S+E+W, column=0, row=6, columnspan=2)
    Grid.rowconfigure(frame, 6, weight=1)
    Grid.columnconfigure(top, 0, weight=1)
    
    keyset = prodList.keys()
    keyList = []
    i=0
    for key in keyset:
            keyList.append(key)
    index=0

    var = StringVar()
    label = Label(top, textvariable=var, relief=RAISED, height=4, width=40, bg="DeepSkyBlue4", fg="white", anchor=CENTER, font=customFont)
    var.set("Please select your destination from below! :) ")
    label.pack()
    
    for x in range(6):
        for y in range (2):
            productname = keyList[index]
            from functools import partial
            btn = Button(frame, width=10, height=5, text=productname, command = partial(show_product, productname), fg="white", bg="red4", anchor=CENTER, font=prodFont)
            index = index + 1
            btn.grid(column=x, row=y, sticky=N+S+E+W)

    for x in range(6):
        Grid.columnconfigure(top, x, weight=1)

    for y in range(6):
        Grid.rowconfigure(top, y, weight=1)

    btn =  Tkinter.Button(grid, width = 10, height = 1, text = "Main Page", command = partial(hideFrame, label), fg="white", bg="red4", anchor=CENTER, font=customFont)
    btn.pack(pady=60, padx=60, expand=True)
        
    frame.pack(fill=BOTH, pady=80, padx=60, expand=True)
  
def show_product(name):
    frame.pack_forget()
    var = StringVar()
    label = Label(top, textvariable=var, relief=RAISED, height=5, width=60, fg="white", bg="red4", anchor=CENTER, font=customFont)
    msg = "Searching for " + name
    var.set(msg)
    label.pack()
    
    
def navigate(name):   
    c.get_route(name)
    
    print name
main_UI()
top.mainloop()
