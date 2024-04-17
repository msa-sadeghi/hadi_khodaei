import sqlite3

con = sqlite3.connect("mydb.db")
cursor = con.cursor()

print("""1> insert product
         2> delete a product
         3> update a product
         4> search a product
         5> show all products
      """)
while True:
    if input(">: ") == "1":
        name = input("enter product name: ")
        price = input("enter product price: ")
        
        
        
     