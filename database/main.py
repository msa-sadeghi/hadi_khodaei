import sqlite3

try:
    conn = sqlite3.connect("online_shop.db")
    print("connected to db")
    cursor = conn.cursor()
    query = """create table if not exists user(
    userid INTEGER not null primary key autoincrement,
    name varchar(100),
    surname varchar(150),
    birthdate date
    );
    """
    cursor.execute(query)
    print("query executed successfuly")
    result = cursor.fetchall()
    print(result)
    cursor.close()
except sqlite3.Error as err:
    print(err)
finally:
    if conn:
        conn.close()
        print("connect closed")