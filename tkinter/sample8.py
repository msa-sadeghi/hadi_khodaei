from datetime import datetime
# f = open("user_log.txt", "a")


# user_name = input("enter the username: ")
# password = input("enter the password: ")
# if user_name == "root" and password == "root":
#     print("user is valid")
#     f.write(f"{user_name} loged in successfully at: {datetime.now()}\n")
# else:
#     print("user is not valid")
#     f.write(f"{user_name} loged in unsuccessfully at: {datetime.now()}\n")
    
# f.close()

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

def register(a,b):
    f = open("user_data.txt", "a")
    f.write(a+",")
    f.write(b+"|")
    f.close()
    


def open_register_window():
    top = tk.Toplevel()
    user_name_text = tk.StringVar()
    password_text = tk.StringVar()
    user_name_label = ttk.Label(top, text="user name", padding=(10,10))
    user_name_label.grid(row=0, column=0)
    user_name = ttk.Entry(top, textvariable=user_name_text)
    user_name.grid(row=0, column=1)
    password_label = ttk.Label(top, text="user name", padding=(10,10))
    password_label.grid(row=1, column=0)
    password = ttk.Entry(top, textvariable=password_text)
    password.grid(row=1, column=1)

    register_button = ttk.Button(top, text="register", command=lambda :register(user_name_text.get(),password_text.get()))
    register_button.grid(row=3, column=0, columnspan=2)
    


def login():
    f = open("user_log.txt", "a")
    if user_name_text.get() == "root" and password_text.get() == "root":
        print("user is valid")
        messagebox.showinfo("status", f"{user_name_text.get()} is valid")
        f.write(f"{user_name_text.get()} loged in successfully at: {datetime.now()}\n")
    else:
        messagebox.showinfo("status", f"{user_name_text.get()} is invalid")
        f.write(f"{user_name_text.get()} loged in unsuccessfully at: {datetime.now()}\n")
    f.close()

root = tk.Tk()

# filename = filedialog.askopenfilename(initialdir="c:/", title="Select a File", filetypes=(("png files", "*.png"),))
clicked = tk.StringVar()
a = ttk.OptionMenu(root,clicked,"Mon", "Tue")
a.grid()
# user_name_text = tk.StringVar()
# password_text = tk.StringVar()
# user_name_label = ttk.Label(root, text="user name", padding=(10,10))
# user_name_label.grid(row=0, column=0)
# user_name = ttk.Entry(root, textvariable=user_name_text)
# user_name.grid(row=0, column=1)
# password_label = ttk.Label(root, text="user name", padding=(10,10))
# password_label.grid(row=1, column=0)
# password = ttk.Entry(root, textvariable=password_text)
# password.grid(row=1, column=1)

# login_button = ttk.Button(root, text="login", command=login)
# login_button.grid(row=2, column=0, columnspan=2)
# register_button = ttk.Button(root, text="register", command=open_register_window)
# register_button.grid(row=3, column=0, columnspan=2)
root.mainloop()



