from my_module import generate_secret_key

def greet():
    print("hello every body")
    if input("do you want to visit secret key:> ").lower().startswith("y"):
        print(generate_secret_key())


greet()


