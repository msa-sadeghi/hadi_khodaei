import tkinter as tk
from tkinter import ttk



root = tk.Tk()
style = ttk.Style(root)
style.theme_use("clam")
style.map("customButton.TButton", foreground=[("pressed", "red"), ("active", "green")], background=[("pressed", "black"),("active", "black")])


my_button = ttk.Button(root, text="hello", style="customButton.TButton")
my_button.grid()

root.mainloop()