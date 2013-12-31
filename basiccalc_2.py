from tkinter import *
from tkinter import ttk

"""
The User Interface class for the calcuator program
"""


class Application():
    # The main container for all the widgets
    mainframe = None
    # The io field for display input and output
    entryScreen = None
    # The text of the io entryScreen
    displayVal = ""
    mag = 0
    prevVal = 0
    currVal = 0
    result = 0
    display = None
    # The buttons for the digits 0 - 9
    numberButtons = []
    # The math operations and other commands
    bAdd = None
    bSubtract = None
    bMultiply = None
    bDivide = None
    bCalculate = None
    # A flag indicating the operation being performed
    opFlag = 0
    # A flag indicating that the previous operation is to be repeated
    repeatFlag = 0
    continueCalFlag = 0

    def __init__(self, master=None):
        self.master = Tk()
        self.master.title = "Basic Calculator"
        self.master.config(width=200, height=200, background="#0000ee")
        self.createWidgets()
        self.master.mainloop()

    def createWidgets(self, master=None):
        #display = StrinVar()
        self.createmainframe(master)
        self.createEntryField()
        self.createButtons()

    def createmainframe(self, master=None):
        self.mainframe = ttk.Frame(master, padding="1 1 1 1")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=0)
        self.mainframe.rowconfigure(0, weight=0)

        # <editor-fold desc="Description">
    def createEntryField(self):
        self.display = StringVar()
        self.entryScreen = ttk.Entry(self.mainframe, width=25, textvariable=self.display)
        self.entryScreen.grid(column=3, row=2, columnspan=4)
        # </editor-fold>

    def createButtons(self):
        self.numberButtons.append(ttk.Button(self.mainframe, text="1", command=lambda: self.modifyDisplay(1), width=4)
            .grid(column=3, row=3))
        self.numberButtons.append(ttk.Button(self.mainframe, text="2", command=lambda: self.modifyDisplay(2), width=4)
            .grid(column=4, row=3))
        self.numberButtons.append(ttk.Button(self.mainframe, text="3", command=lambda: self.modifyDisplay(3), width=4)
            .grid(column=5, row=3))
        self.numberButtons.append(ttk.Button(self.mainframe, text="4", command=lambda: self.modifyDisplay(4), width=4)
            .grid(column=3, row=4))
        self.numberButtons.append(ttk.Button(self.mainframe, text="5", command=lambda: self.modifyDisplay(5), width=4)
            .grid(column=4, row=4))
        self.numberButtons.append(ttk.Button(self.mainframe, text="6", command=lambda: self.modifyDisplay(6), width=4)
            .grid(column=5, row=4))
        self.numberButtons.append(ttk.Button(self.mainframe, text="7", command=lambda: self.modifyDisplay(7), width=4)
            .grid(column=3, row=5))
        self.numberButtons.append(ttk.Button(self.mainframe, text="8", command=lambda: self.modifyDisplay(8), width=4)
            .grid(column=4, row=5))
        self.numberButtons.append(ttk.Button(self.mainframe, text="9", command=lambda: self.modifyDisplay(9), width=4)
            .grid(column=5, row=5))
        self.numberButtons.append(ttk.Button(self.mainframe, text="0", command=lambda: self.modifyDisplay(0), width=4)
            .grid(column=4, row=6))
        #//create math funtions buttons (+,-,*,/,=)\\
        self.bAdd = ttk.Button(self.mainframe, text="+", command=lambda: self.add(), width=4).grid(column=6, row=3)
        self.bSubtract = ttk.Button(self.mainframe, text="-", command=lambda: self.subtract(), width=4).grid(column=6, row=4)
        self.bMultiply = ttk.Button(self.mainframe, text="*", command=lambda: self.multiply(), width=4).grid(column=6, row=5)
        self.bDivide = ttk.Button(self.mainframe, text="/", command=lambda: self.divide(), width=4).grid(column=6, row=6)
        self.bCalculate = ttk.Button(self.mainframe, text="=", command=lambda: self.calculate(), width=25).grid(column=1, row=7, columnspan=9)

    # Change the value of the display to reflect user input
    def modifyDisplay(self, value):
        # Make sure not to display leading 0, which is necessary to make int() work for all inputs
        if self.displayVal == "0":
            self.displayVal = str(value)
            self.repeatFlag = 0
        else:
            self.displayVal += str(value)
        self.mag += 1
        self.display.set(self.displayVal)

    """def commandListener(self):
        if continueCalFlag == 1:
            self.bCalculate.invoke()
        else:
            self.addHandler(self.opFlag)
     """


    def add(self):
        self.opFlag = "ADD"
        self.set()
    def subtract(self):
        self.opFlag = "SUB"
        self.set()
    def multiply(self):
        self.opFlag = "MUL"
        self.set()
    def divide(self):
        self.opFlag = "DIV"
        self.set()
    def calculate(self):
        if self.repeatFlag == 1:
            self.prevVal = self.result
        else:
            self.currVal = int(self.displayVal)
            self.repeatFlag = 1

        if self.opFlag == "ADD":
            self.result = Math.add(self, n1=self.prevVal, n2=self.currVal)
        if self.opFlag == "SUB":
            self.result = Math.subtract(self, self.prevVal, self.currVal)
        if self.opFlag == "MUL":
            self.result = Math.multiply(self, self.prevVal, self.currVal)
        if self.opFlag == "DIV":
            self.result = Math.divide(self, self.prevVal, self.currVal)

        self.displayVal = str(self.result)
        self.display.set(self.displayVal)
        self.displayVal = "0"

    def set(self):
        self.repeatFlag = 0
        if self.repeatFlag == 1:
            self.calculate()
        else:
            self.repeatFlag = 1
            self.prevVal = int(self.displayVal)
            self.displayVal = "0"
            self.mag = 0


#class CalculatorView
class Math():
    def add(self, n1, n2):
        return n1 + n2
    def subtract(self, n1, n2):
        return n1 - n2
    def multiply(self, n1, n2):
        return n1 * n2
    def divide(self, n1, n2):
        return n1 / n2





app = Application()
