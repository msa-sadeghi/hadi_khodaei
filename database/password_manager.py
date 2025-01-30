import sqlite3
import getpass
from cryptography.fernet import Fernet



# key = Fernet.generate_key()
key = b'lkUx_Pb_1YEVTjO4IfFd-2C1GVNUc7S9SZsrraETUic='
f = Fernet(key)



conn = sqlite3.connect("password_manager.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS password(
    id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    website TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
               ''')
cursor.execute('''CREATE TABLE IF NOT EXISTS user(
    id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
               ''')



def register_user():
    username = input("enter your username: ")
    password = getpass.getpass("Enter your password: ")
    encrypted_password = f.encrypt(password.encode()).decode()
    cursor.execute("INSERT INTO user (username, password) VALUES (?,?)", (username, encrypted_password))
    conn.commit()
    print("user registration successful!")

# register_user()  
# def login():
    
# generate_strong_password
# change_password -> user must be loged in and can nt change other users password
