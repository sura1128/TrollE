#GUI

from Controller import Controller
c = Controller({})
c.setup()

from Imu import IMU
i = IMU()


prodList = c.get_product_map()

from Tkinter import *
import Tkinter
import tkMessageBox
import ttk
import tkFont

from PIL import ImageTk, Image
img = ImageTk.PhotoImage(Image.open("fresh-produce.png"))

top = Tkinter.Tk()
top.minsize(width=500, height=500)
frame = Frame(top)
grid = Frame(frame)

myvar=Label(top, image=img)
myvar.place(x=0,y=0,relwidth=1, relheight=1)

top.configure(bg='peach puff')
customFont = tkFont.Font(family="Cambria", size=14)
prodFont = tkFont.Font(family="Cambria", size=12)

#Product List
LBox = Listbox(top, height=10, width=20, fg="DeepSkyBlue4", bg="peach puff", font=customFont)

#Product Label
var = StringVar()
label = Label(top, textvariable=var, relief=RAISED, height=2, width=60, fg="white", bg="IndianRed2", anchor=CENTER, font=customFont)




def main_UI():
    #Welcome Message
    var = StringVar()
    label = Label(top, textvariable=var, relief=RAISED, height=5, width=60, fg="white", bg="IndianRed2", anchor=CENTER, font=customFont)
    var.set("WELCOME TO TROLL-E! How can we help you today? >^^<")
    label.pack(pady=60, padx=30)
    #Show Products Button
    w = Tkinter.Button (top, width = 20, height = 4, text = "Show Products!", command = searchBox, bg="medium aquamarine", fg="white", font=customFont)
    w.pack(pady=60, padx=60, side=LEFT)
    
    b = Tkinter.Button (top, width = 20, height = 4, text = "Plan Budget!", command = budget, bg="medium aquamarine", fg="white", font=customFont)
    b.pack(pady=60, padx=60, side=RIGHT)


def budget():
    print "hello"
    
def hideFrame(label):
    frame.pack_forget()
                

def searchBox():
    LBox.delete(0, END)
    LBox.pack_forget()
    label.pack_forget()
    
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
    
    for x in range(6):
        for y in range (2):
            productname = keyList[index]
            from functools import partial
            btn = Button(frame, width=10, height=5, text=productname, command = partial(show_product, productname), fg="white", bg="firebrick4", anchor=CENTER, font=prodFont)
            index = index + 1
            btn.grid(column=x, row=y, sticky=N+S+E+W)

    for x in range(6):
        Grid.columnconfigure(top, x, weight=1)

    for y in range(6):
        Grid.rowconfigure(top, y, weight=1)
        
    frame.pack(fill=BOTH, pady=80, padx=60, expand=True)
  
def show_product(name):
    frame.pack_forget()
    var.set(name + "\n" + "Currently facing: North")
    label.pack()

    if name!="Checkout":
    
        LBox.insert(1, "In Stock: ")
        LBox.insert(2, " ")
        i = 3
        items = c.getItems(name)
        keyset = items.keys()
        for key in keyset:
            LBox.insert(i, key)
            i=i+1
        LBox.pack()
    
    
def navigate(name):   
    c.get_route(name)
    
    print name
main_UI()
top.mainloop()
