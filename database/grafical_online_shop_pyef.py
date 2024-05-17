import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3
from db import *

con = sqlite3.connect("online_shop.db")
cursor = con.cursor()

root = tk.Tk()
root.title("Online shop")
root.geometry("300x330")

welcom_label = ttk.Label(root, text="Welcom to Online shop")
welcom_label.place(relx=0.5, rely=0.2, anchor=CENTER)

product_name_text = tk.StringVar()
product_price_text = tk.StringVar()

def bla(x):
    print(x)


def open_insert_window():
    win = tk.Toplevel(root)
    win.title("Insert Window")
    win.geometry("247x150")

    product_name_label = ttk.Label(win, text="Enter product name: ")
    product_name_label.grid(row=1, column=1)

    product_name = ttk.Entry(win, textvariable=product_name_text)
    product_name.grid(row=1, column=2)

    product_price_label = ttk.Label(win, text="Enter product price: ")
    product_price_label.grid(row=2, column=1)

    product_price = ttk.Entry(win, textvariable=product_price_text)
    product_price.grid(row=2, column=2)

    insert_button = ttk.Button(win, text="insert", command=lambda n=product_name_text.get(), p=product_price_text.get(), t="products":insert_into_table(t, con, cursor, product_name=n, product_price=p))
    insert_button.place(relx=0.5, rely=0.8, anchor=CENTER)
    insert_button = ttk.Button(win, text="show", command=lambda :insert_into_table("products", con, cursor,product_name= product_name_text.get(), product_price=product_price_text.get()))
    insert_button.place(relx=0.8, rely=0.9, anchor=CENTER)
    

"""
    0>Exit
    1> insert product
    2> delete a product
    3> update a product
    4> search a product
    5> show all products
"""

exit_button = ttk.Button(root, text="Exit", command=root.destroy)
exit_button.grid(row=3, column=1)

insert_button = ttk.Button(root, text="Insert", command=open_insert_window)
insert_button.grid(row=3, column=2)

root.mainloop()