from online_shop import *


def register_new_user():
    """this function is for registering a new user
   
    """
    name = input("enter your name: ")
    familyname = input("enter your familyname: ")
    birthdate = input("enter your birthdate:(2023-02-02) ")
    address = input("enter your address: ")
    phonenumber = input("enter your phonenumber: ")
    email = input("enter your email: ")
    password = input("enter your password: ")
    gender = input("enter your gender: (w or m)")
    if gender == "m":
        gender_id = get_id("gender", "gender","man")
    elif gender =="w":
        gender_id = get_id("gender", "gender","woman")
    city = input("enter your city: ")
    city_id = get_id("city", "name",city)


    new_user = {
        "name":name, 
        "familyname":familyname, 
        "birthdate":birthdate, 
        "address":address,
        "phonenumber":phonenumber,
        "email":email,
        "password":password,
        "gender_id":gender_id, 
        "city_id":city_id, 
    
    }   
    user_id = insert_into_user(new_user)
    add_credit_card(user_id)

def add_credit_card(user_id):
    """This function is used to add credit card to specific user

    Args:
        user_id (int): user's id
    """
    card_number = input("enter creditcard number: ")
    cvv2 = input("enter creditcard cvv2: ")
    expire_month = input("enter creditcard expire_month: ")
    expire_year = input("enter creditcard expire_year: ")
    cardtype = input("enter your cardtype:(etebari = 1, banki = 2) ")
    if cardtype == "1":
        cardtype = "etebari"
    elif cardtype == "2":
        cardtype = "banki"
    cardTypeId = get_id("cardtype", "name",cardtype)
    credit_card = {
        "number":card_number, 
        "cvv2":cvv2, 
        "expire_month":expire_month, 
        "expire_year":expire_year,
        "cardTypeId":cardTypeId,
        "user_id":user_id
    }   
    credit_card_id = insert_into_credit_card(credit_card)
    
def add_manufactor():
    name = input("enter manufactor name: ")
    url = input("enter manufactor url: ")
    
    
#manufactor
#branch
#stock
#order