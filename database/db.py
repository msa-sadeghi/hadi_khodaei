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


def insert_into_table(table_name, **kwargs):
    all_fields = list(kwargs.items())
    print(all_fields)
    con = sqlite3.connect("online_shop.db")
    cursor = con.cursor()
    vals = ""
    query = f"INSERT INTO {table_name} ("
    for tup in all_fields:
        query += tup[0] + ","
        vals += str(tup[1])
    query = query[:-1] + ") " + "VALUES ("
    print(query)
    print(vals)
    
insert_into_table("products", product_name="blalalal", product_price=1234)