from tkinter import *

def frame(root, side):
    w = Frame(root)
    w.pack(side=side, expand=True, fill=BOTH)
    return w


def button(root, side, text, command=None):
    w = Button(root, text=text, command=command)
    w.pack(side=side, expand=True, fill=BOTH)
    return w

class Calculator(Frame):
    def __init__(self):
        super().__init__()
        self.pack(expand=True, fill=BOTH)
        self.master.title("Simple Calculator")
        
        self.option_add('*Font', 'Terminal 12')
        display = StringVar()
        Entry(self, relief=SUNKEN, textvariable=display).pack(side=TOP, expand=True, fill=BOTH)
        
        for key in ("123", "456", "789", "-0."):
            keyF = frame(self, TOP)
            for char in key:
                button(keyF, LEFT, char, lambda w=display, c=char: w.set(w.get()+c))
                
        opsF = frame(self, TOP)
        for char in "+-*/=":
            if char == "=":
                button(opsF,LEFT, char, lambda w=display: self.calc(w))
                self.master.bind('<Return>', lambda e,w=display: self.calc(w))
            else:
                button(opsF, LEFT, char, lambda w=display, s=char:w.set(w.get()+s))
                
        clearF = frame(self, BOTTOM)
        button(clearF, LEFT, 'Clr', lambda w=display:w.set(''))
        
    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")
                
            
        
        
Calculator().mainloop()