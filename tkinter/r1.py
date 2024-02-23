from tkinter import *

root = Tk()

text = Text(root)
text.pack()
text.insert(1.0, 'blalalalalla')
text.insert(END, '\n')
text.insert(END, 'lalalallaanabbabaab')
root.mainloop()