import sqlite3
from db import *
con = sqlite3.connect("mydb.db")
cursor = con.cursor()

def search():
    name = input("enter product name: ")
    price = input("enter product price: ")
    if price:
        return(search_from_table("products", product_name=name, product_price=price))
    else:
        return(search_from_table("products", product_name=name))
con, cursor = open_connection_to_db("online_shop.db")

print("""0>Exit
         1> insert product
         2> delete a product
         3> update a product
         4> search a product
         5> show all products
      """)
while True:
    user_input = input(">: ")
    if user_input == "0":
        exit()
    if user_input == "1":
        name = input("enter product name: ")
        price = input("enter product price: ")
        insert_into_table("products",con,cursor, product_name=name, product_price=price)
        print(f"product {name}, Added Successfully.")
    if user_input == "2":
        res = search()
        print(res)
        
        
    if user_input == "4":
        search()
    if user_input == "5":
        records  = show_all_records("products")
        for record in records:
            print(record)
            
        
        
        
        
        
     