from tkinter import *
import Pmw, string

class SLable(Frame):
    def __init__(self, master, leftl, rightl):
        super.__init__(bg='gray40')
        self.pack(side=LEFT, expand=True, fill=BOTH)
        Label(self, text=leftl, fg='steelblue1', font=("arial", 6, "bold"),\
            width=5, bg='gray40').pack(side=LEFT, expand=True, fill=BOTH)
        Label(self, text=rightl, fg='white', font=("arial", 6, "bold"),\
            width=5, bg='gray40').pack(side=RIGHT, expand=True, fill=BOTH)
        
class Key(Button):
    def __init__(self, master, font=('arial', 8, 'bold'), fg='white', width=5, borderwidth=5, **kw):
        kw['font'] = font
        kw['fg'] = fg
        kw['width'] = width
        kw['borderwidth'] = borderwidth
        super().__init__(master, kw)
        self.pack(side=LEFT, expand=False, fill=NONE)
        
class Calculator(Frame):
    def __init__(self, parent = None):
        super().__init__(bg='gray40')
        self.pack(expand=True, fill=BOTH)
        self.calc = Evaluator()
        
        self.buildCalculator()
        
        self.current = ""
        
    def turnoff(self, *args):
        self.quit()
    def clearall(self, *args):
        self.current = ""
        self.display.component('text').delete(1.0, END)
    def doEnter(self, *args):
        result = self.calc.runpython(self.current)
        if result:
            self.display.insert(END, '\n')
            self.display.insert(END, f'{result}\n')
        self.current = ""
        
    def doKeyPress(self, event):
        pass
        
    
    def buildCalculator(self):
        self.display = Pmw.ScrolledText(self, hsrcollmode='dynamic',\
            vsrcollmode= 'dynamic', text_background="honeydew4", \
                text_foreground="black", text_font=('arial', 12, 'bold'))
        self.display.pack(side = TOP, expand= True, fill= BOTH)
        self.display.component('text').bind('<Key>', self.doKeyPress)
        self.display.component('text').bind('<Return>', self.doEnter)
        
        
        
        
class Evaluator:
    def __init__(self):
        self.runpython("from math import *")
    
    def runpython(self, code):
        try:
            return eval(code)
        except SyntaxError:
            try:
                exec(code)
            except:
                return 'Error'
            
Calculator().mainloop()
        
        
    