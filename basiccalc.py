
from tkinter import *
from tkinter import ttk
#define 1-9
def n1(*args):
    try:
        display == 1
        
    except ValueError:
        pass
def n2(*args):
    try:
        display == 2
    except ValueError:
        pass
def n3(*args):
    try:
        display == 3
    except ValueError:
        pass
def n4(*args):
    try:
        display == 4
    except ValueError:
        pass
def n5(*args):
    try:
        display == 5
    except ValueError:
        pass
def n6(*args):
    try:
        display == 6
    except ValueError:
        pass
def n7(*args):
    try:
        display == 7
    except ValueError:
        pass
def n8(*args):
    try:
        display == 8
    except ValueError:
        pass
def n9(*args):
    try:
        display == 9
    except ValueError:
        pass
def n0(*args):
    try:
        display == 0
    except ValueError:
        pass
#//create the window\\
window =Tk()
#window.geometry('150x150+200+50')
window.title("basiccalc")
mainframe=ttk.Frame(window, padding="1 1 1 1")

mainframe.grid(column=0,row=0,sticky=(N, W, E, S),)
mainframe.columnconfigure(0,weight=0)
mainframe.rowconfigure(0,weight=0,)
#//create the numbers display\\
display = StringVar()
entryscreen=ttk.Entry(mainframe, width=25, textvariable=display)
entryscreen.grid(column=3, row=2,columnspan=4)
#//create buttons 1-9\\
ttk.Button(mainframe, text="1" ,command=n1,width = 4).grid(column=3, row=3)
ttk.Button(mainframe, text="2" ,command=n2,width = 4).grid(column=4, row=3)
ttk.Button(mainframe, text="3" ,command=n3,width = 4).grid(column=5, row=3)
ttk.Button(mainframe, text="4" ,command=n4,width = 4).grid(column=3, row=4)
ttk.Button(mainframe, text="5" ,command=n5,width = 4).grid(column=4, row=4)
ttk.Button(mainframe, text="6" ,command=n6,width = 4).grid(column=5, row=4)
ttk.Button(mainframe, text="7" ,command=n7,width = 4).grid(column=3, row=5)
ttk.Button(mainframe, text="8" ,command=n8,width = 4).grid(column=4, row=5)
ttk.Button(mainframe, text="9" ,command=n9,width = 4).grid(column=5, row=5)
ttk.Button(mainframe, text="0" ,command=n0,width = 4).grid(column=4, row=6)
#//create math funtions buttons (+,-,*,/,=)\\
ttk.Button(mainframe, text="+" ,command=n1,width = 4).grid(column=6, row=3)
ttk.Button(mainframe, text="-" ,command=n2,width = 4).grid(column=6, row=4)
ttk.Button(mainframe, text="*" ,command=n3,width = 4).grid(column=6, row=5)
ttk.Button(mainframe, text="/" ,command=n4,width = 4).grid(column=6, row=6)
ttk.Button(mainframe, text="=" ,command=n5,width = 25).grid(column=1, row=7,columnspan =9)

#//padd all widgets\\
#/for child in mainframe.winfo_children():child.grid_configure(padx=1,pady=1)
#display.focus()
#//tie objects and funct everything together\\
#window.config(width=200, height=200,background="#0000ee")
window.mainloop();
