import tkinter as tk
from tkinter import ttk

class UserInputForm(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.user_input = tk.StringVar()
        label = ttk.Label(self, text="Enter username:")
        label.pack(side="left")
        entry = ttk.Entry(self, textvariable=self.user_input)
        entry.pack(side="left")
        button = ttk.Button(self, text="submit", command=self.submit)
        button.pack()
        
    def submit(self):
        print(f"Hello {self.user_input.get()}")
        

root = tk.Tk()
frame = UserInputForm(root)

frame.pack()
frame = UserInputForm(root)

frame.pack()
root.mainloop()