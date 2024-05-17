import sqlite3
import datetime

def create_database(db_name):
    """This function is used to create a database

    Args:
        db_name (str): database name
    """
    try:
        conn = sqlite3.connect("online_shop.db")
    except sqlite3.Error as err:
        print(err)
    finally:
        conn.close()
        
def create_table(table_name, **kwargs):
    """
    """
    all_fields = list(kwargs.values())
    try:
        conn = sqlite3.connect("online_shop.db")
        print(f"connected to online_shop db")
        cursor = conn.cursor()
        
        query = f"""create table if not exists {table_name}(
        id INTEGER not null primary key autoincrement,
        """
        for field in all_fields:
            query += f"{field} varchar(100)," 
        else:
            query = query[:-1]         
        query += ");"
        print(query)
        cursor.execute(query)
        print("query executed successfuly")
        conn.commit()
    except sqlite3.Error as err:
        print(err)
    finally:
        conn.close()
    
create_table("products", 
             field_1="product_name", 
             field_2="product_price",
             )

def open_connection_to_db(db_name):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    return con, cursor
    

def insert_into_table(table_name,con, cursor, **kwargs):
    all_fields = list(kwargs.items())
    print("****************************,insert_into_table ")
    print(table_name)
    print(con)
    print(cursor)
    print(all_fields)
    vals = ""
    query = f"INSERT INTO {table_name} ("
    for tup in all_fields:
        query += tup[0] + ","
        vals += '"' + str(tup[1])  + '"' + ","
    vals = vals[:-1]
    query = query[:-1] + ") " + "VALUES ("
    query += vals + ")" 
    cursor.execute(query)
    con.commit()   

def search_from_table(table_name,**kwargs):
    con = sqlite3.connect("online_shop.db")
    all_fields = list(kwargs.items())
    cursor = con.cursor()
    query = f"""SELECT * from {table_name} WHERE """
    for field in all_fields:
        query += field[0] + "="  +'"' + field[1] + '"' + " and "
    else:
        query = query[:-5]
    qs = list(cursor.execute(query))
    return qs
 
def delete_from_table(table_name, id):
    res = None
    try:
        con = sqlite3.connect("online_shop.db")
        cursor = con.cursor()
        query = f"DELETE FROM {table_name} WHERE id={id}"
        cursor.execute(query)
        con.commit()
        res = "SUCCESS"
    except sqlite3.DatabaseError as er:
        res = "FAILURE"
    finally:
        con.close()
    return res
    
def update_product(table_name, **kwargs):
    name = input("enter product new name: ")
    price = input("enter product new price: ")
    info = list(kwargs.items())
    con, cursor = open_connection_to_db("online_shop.db")
    query = f'UPDATE {table_name} SET product_name="{name}", product_price="{price}" WHERE product_name="{info[0][1]}" AND product_price="{info[1][1]}"'
    print(query)
    try:
        cursor.execute(query)
        con.commit()
    except sqlite3.DatabaseError as err:
        print(err)
        
    
   
def show_all_records(table_name):
    con = sqlite3.connect("online_shop.db")
   
    cursor = con.cursor()
    query = f"""SELECT * from {table_name}"""
    qs = list(cursor.execute(query))
    return qs


def hi(n1,n2,n3,n4):
    print(n1,n2,n3,n4)