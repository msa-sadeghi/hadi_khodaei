import sqlite3
import tkinter
from tkinter import ttk

root = tkinter.Tk()
style = ttk.Style()
style.theme_use('default')
style.configure("Treeview", background = "#efefef", foreground="black")
style.map('TreeView', background=[('selected', "#347083")])
tree_frame = ttk.Frame(root)
tree_frame.pack(pady=10)
tree_scroll = ttk.Scrollbar(tree_frame)
tree_scroll.pack(side="right", fill="y")
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

tree_scroll.config(command=my_tree.yview)

my_tree['columns'] = ("id", "product_name", "product_price")
my_tree.column("#0", width=0, stretch="no")
my_tree.column("id", anchor="w", width=140)
my_tree.column("product_name", anchor="w", width=140)
my_tree.column("id", anchor="w", width=140)

my_tree.heading("#0", text="", anchor="w")
my_tree.heading("id", text="id", anchor="w")
my_tree.heading("product_name", text="Name", anchor="w")
my_tree.heading("product_price", text="Price", anchor="w")

con = sqlite3.connect("online_shop.db")
cursor = con.cursor()

query = "SELECT * FROM products"
cursor.execute(query)
products = cursor.fetchall()

my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")


for i,product in enumerate(products):
    if i % 2 == 0:
        my_tree.insert(parent='', index='end', values=(product[0], product[1], product[2]), tags=('evenrow'))
    else:
        my_tree.insert(parent='', index='end', values=(product[0], product[1], product[2]), tags=('oddrow'))


# add record to treeview
data_frame = ttk.LabelFrame(root, text="Record")
data_frame.pack(fill="x", expand=True,padx=20)
product_name_label = ttk.Label(data_frame, text="Product Name")
product_name_label.grid(row=0, column=0, padx=10, pady=10)


root.mainloop()