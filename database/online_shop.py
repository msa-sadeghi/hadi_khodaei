from mysql.connector import connect
from datetime import date

conn = connect(host="localhost", user="root",password="root", database="online_shop")


def show_all_users():
    cursor = conn.cursor()
    query = "SELECT * FROM user"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result


def insert_into_user(kwargs):
    cursor = conn.cursor()
    
    query = f'''INSERT INTO user (name, familyname, birthdate, address, phonenumber, email,password, gender_id, city_id) Values (%s, %s, %s,%s, %s,%s, %s,%s, %s)'''
    val = (kwargs["name"],kwargs["familyname"],kwargs["birthdate"],kwargs["address"],kwargs["phonenumber"],
            kwargs["email"], kwargs["password"],kwargs["gender_id"],kwargs["city_id"])
    cursor.execute(query, val)
    conn.commit()
    res = cursor.lastrowid
    cursor = conn.cursor()
    return res
def insert_into_credit_card(kwargs):
    cursor = conn.cursor()
    
    query = f'''INSERT INTO creditcard (number, cvv2, expire_month, expire_year, cardTypeId, user_id) Values (%s, %s, %s,%s, %s, %s)'''
    val = (kwargs["number"],kwargs["cvv2"],kwargs["expire_month"],kwargs["expire_year"],kwargs["cardTypeId"], kwargs["user_id"])
    cursor.execute(query, val)
    conn.commit()
    res= cursor.lastrowid
    return res
    
def get_id(t,f,v)    :
    cursor = conn.cursor()
    print(t,f,v)
    print(cursor)
    
    try:
        if t == "city":
            query = f"SELECT id FROM {t} WHERE {f} Like %s"
            cursor.execute(query,(f"%{v}%",))
        else:   
            
            query = f"SELECT id FROM {t} WHERE {f} = %s"
            cursor.execute(query,(f"{v}",))
        
        # conn.commit()
    except Exception as ex:
        print(ex)
    res = cursor.fetchone()[0]
    
    
    return res
    

def insert_into_manufactor(name, url):
    