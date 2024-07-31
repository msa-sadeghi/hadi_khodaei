import psycopg2

con = psycopg2.connect(
    host="localhost",
    port="5432",
    database="test", 
    user="postgres", 
    password="root"
)

cursor = con.cursor()
query = "SELECT * FROM myuser"
res = cursor.execute(query)
res = cursor.fetchone()
user_name = res[1]
passw = res[2]
user_input = input("enter the username: ")
p = input("enter the password: ")
if user_name == user_input and passw == p:
    print("login success")
else:
    print("user is not ...")
    