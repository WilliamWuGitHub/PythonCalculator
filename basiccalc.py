from tkinter import *
from tkinter import ttk

"""
The User Interface class for the calcuator program
"""

debug = 0
class Calculator():
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
    opFlag = "None"
    # A flag indicating that the previous operation is to be repeated
    repeatFlag = 0
    continueCalFlag = 0

    def __init__(self, master=None):
        self.master = Tk()
        self.master.title = "Basic Calculator"
        self.master.config(width=200, height=200, background="#0000ee")
        self.createWidgets()
        if not debug:
            self.master.mainloop() #start the gui


    # This section is used to create the gui for the calculator
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
    #  ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    # Change the value of the display to reflect user input
    def modifyDisplay(self, value):
        # Make sure not to display leading 0, which is necessary to make int() work for all inputs


        self.displayVal += str(value)
        self.mag += 1
        self.display.set(self.displayVal)

    """def commandListener(self):
        if continueCalFlag == 1:
            self.bCalculate.invoke()
        else:
            self.addHandler(self.opFlag)
     """

    # These functions change the operation state of the calculator
    def add(self):
        self.set()
        self.opFlag = "ADD"

    def subtract(self):
        self.set()
        self.opFlag = "SUB"
    def multiply(self):
        self.set()
        self.opFlag = "MUL"
    def divide(self):
        self.set()
        self.opFlag = "DIV"

    # This executes the current operation
    # Pre: opFlag is defined
    # Post: changes the value of result to indicate the new result from performing the current operation
    #       of prevVal and currVal
    #       if the button is pressed for the first time it performs the current operation in memory
    #       if pressed successively thereafter, it will redo the operation using the result and the last value of
    #       currVal. Display val will also be reset to ""
    def calculate(self):

        # Test to see if it is being pressed repeatedly
        if not self.repeatFlag == 0:
            self.prevVal = self.result
        else:
            self.currVal = int(self.displayVal)
            self.repeatFlag = 1

        # Determine the operation state calculator is set to
        if self.opFlag == "ADD":
            self.result = Math.add(self, self.prevVal, self.currVal)
        if self.opFlag == "SUB":
            self.result = Math.subtract(self, self.prevVal, self.currVal)
        if self.opFlag == "MUL":
            self.result = Math.multiply(self, self.prevVal, self.currVal)
        if self.opFlag == "DIV":
            self.result = Math.divide(self, float(self.prevVal), float(self.currVal))

        self.displayVal = str(self.result)
        self.display.set(self.displayVal)
        self.displayVal = "0"
        # reset the state of the calculator


    # A helper function for the operation state modifiers
    # Pre: none
    # Post: sets the state of the calculator
    #       the methods behaves in two ways
    #       if the users has not pressed calculate after entering initial prevVal op currVal sequence
    #       the calculation will be performed and the result will become the new preVal
    def set(self):

        # The user enters an expression with more than two terms we need to update the display
        if self.opFlag == "None":
            self.prevVal = int(self.displayVal)
            self.displayVal = "0"
            self.continueCalFlag = 1
            self.mag = 0
        else:
            self.prevVal = self.result
            self.currVal = int(self.displayVal)
            self.calculate()
        self.repeatFlag = 0





#/\\\\\\\\\\\\\\\\\\\class CalculatorView

"""
Math class
    Contains the algorithms for each calculator operation
"""
class Math():
    def add(self, n1, n2):
        return n1 + n2
    def subtract(self, n1, n2):
        return n1 - n2
    def multiply(self, n1, n2):
        return n1 * n2
    def divide(self, n1, n2):
        return float(n1) / n2




if debug:
    pass
else:
    app = Calculator()

