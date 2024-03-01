from tkinter import *
import Pmw, string

class SLable(Frame):
    def __init__(self, master, leftl, rightl):
        super().__init__(master, bg='gray40')
        self.pack(side=LEFT, expand=True, fill=BOTH)
        Label(self, text=leftl, fg='steelblue1', font=("arial", 6, "bold"),\
            width=5, bg='gray40').pack(side=LEFT, expand=True, fill=BOTH)
        Label(self, text=rightl, fg='white', font=("arial", 6, "bold"),\
            width=1, bg='gray40').pack(side=RIGHT, expand=True, fill=BOTH)
        
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
        self.actionDict = {
            'log' : self.do_this,
            'sin' : self.do_this,
            'cos' : self.do_this,
            'enter' : self.do_this,
        }
    
    def do_this(self, action):
        
        if action == "enter":
            self.doEnter()
        else:
            print(f"has not been implemented {action} yet")
            
       
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
        key = event.char
        self.current += key
    def keyAction(self, key)   :
        self.display.insert(END, key)
        self.current += key
    def evalAction(self, action):
        try:
            self.actionDict[action](action)
        except:
            pass
        
    
    def buildCalculator(self):
        
        FUN = 1
        KEY = 0
        KC1 = 'gray30'
        KC2 = 'gray50'
        KC3 = 'steelblue1'
        KC4 = 'steelblue'
        keys = [
            [
                ('Log', '10x', 'N', KC1, FUN, 'log'),
                ('7', '10x', 'N', KC2, KEY, '7'),
                ('8', '10x', 'N', KC2, KEY, '8'),
                ('9', '10x', 'N', KC2, KEY, '9'),
                ('X', '[', 'N', KC4, KEY, '*'),
            ],
            [
                ('Ln', 'ex', 'N', KC1, FUN, 'ln'),
                ('4', '10x', 'N', KC2, KEY, '4'),
                ('5', '10x', 'N', KC2, KEY, '5'),
                ('6', '10x', 'N', KC2, KEY, '6'),
                ('-', ']', 'N', KC4, KEY, '-'),
            ],
            [
                ('Ln', 'ex', 'N', KC1, FUN, 'ln'),
                ('1', '10x', 'N', KC2, KEY, '1'),
                ('2', '10x', 'N', KC2, KEY, '2'),
                ('3', '10x', 'N', KC2, KEY, '3'),
                ('+', ']', 'N', KC4, KEY, '+'),
            ],
            [
                ('Off', 'ex', 'N', KC1, FUN, 'off'),
                ('0', '10x', 'N', KC2, KEY, '0'),
                ('.', '10x', 'N', KC2, KEY, '.'),
                ('(-)', '10x', 'N', KC2, FUN, 'neg'),
                ('Enter', ']', 'N', KC4, FUN, 'enter'),
            ],
            
        ]
        
        self.display = Pmw.ScrolledText(self, hscrollmode='dynamic',\
            vscrollmode= 'dynamic', text_background="honeydew4", \
                text_foreground="black", text_font=('arial', 12, 'bold'), text_height=6,text_width=16)
        self.display.pack(side = TOP, expand= True, fill= BOTH)
        self.display.component('text').bind('<Key>', self.doKeyPress)
        self.display.component('text').bind('<Return>', self.doEnter)
        
        for row in keys:
            rowa = Frame(self, bg='gray40')
            rowb = Frame(self, bg='gray40')
            for p1, p2, p3, color, ktype, func in row:
                if ktype == FUN:
                    a = lambda s = self, a=func :s.evalAction(a)
                else:
                    a = lambda s = self, k=func :s.keyAction(k)
                    
                SLable(rowa, p2, p3)
                Key(rowb, text=p1, bg=color, command=a)
            rowa.pack(side=TOP, expand=True, fill=BOTH)
            rowb.pack(side=TOP, expand=True, fill=BOTH)
            
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
        
        
    