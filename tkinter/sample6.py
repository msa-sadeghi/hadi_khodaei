import tkinter as tk
from tkinter import ttk

def greet():
    print(f'Hello,{user_name.get()}')
    

root = tk.Tk()

style = ttk.Style(root)
# print(style.theme_names())
# print(style.theme_use())
style.theme_use('clam')

print(style.layout("TLabel"))
print(style.element_options("Label.border"))
print(style.element_options("Label.padding"))
print(style.element_options("Label.label"))
print(style.lookup("TLabel", "font"))
print(style.lookup("TLabel", "foreground"))
print(style.lookup("TLabel", "compound"))
style.configure("customStyle.TLabel",bordercolor="#f00",borderwidth=20,relief="solid", font=("Arial", 22))

main = ttk.Frame(root, padding=(40,20))
main.grid()

user_name = tk.StringVar()
name_label = ttk.Label(main, text="Username:")
name_label["style"] = "customStyle.TLabel"
# print(name_label.winfo_class())
name_label.grid(row=0, column=0, padx=(0,10))
name_entry = ttk.Entry(main, width=15, textvariable=user_name)
name_entry.grid(row=0, column=1, padx=10)
name_entry.focus()
greet_button = ttk.Button(main, text="Greet", command=greet)
greet_button.grid(row=0, column=2, sticky="ew", padx=10)

my_label = ttk.Label(main, text="my label")
my_label.grid(row=1, column=1)


root.mainloop()


