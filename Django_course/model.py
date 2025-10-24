class User:
    def __init__(self, username, email):
        self.username = username
        self.email =  email
        self.is_active = True

    def deactivate(self):
        self.is_active = False
        print(f"{self.username} deactived.")

    def get_info(self):
        return f"username: {self.username}, email :{self.email}"
    
class Product:
    total_products = 0
    def __init__(self,name, price, category, stock=0):
        self.id = Product.total_products + 1
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock
        Product.total_products += 1

    def is_available(self):
        return self.stock > 0
    
    def sell(self, quantity = 1):
        if quantity > self.stock:
            return {"success": False, "message": "not exists in stock"}
        self.stock -= quantity
        total_price = self.price * quantity
        return {
            "success" : True,
            "message" : f"{quantity} number {self.name} selled",
            "total" : total_price
        }
    def __str__(self):
        return f"id:{self.id}, name:{self.name}"
    def __repr__(self):
        return f"id:{self.id}, name:{self.name}"
    

products = []
for i in range(3):
    p = Product("lap", "100", "elec", 1)
    products.append(p)

print(products)
# with open("products.json", "w", encoding = "utf-8") as f:


class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.__balance= initial_balance
        self.__transactions = []

    def deposit(self, amount):
        if amount <= 0:
            return "you cant deposit 0"
        self.__balance += amount
        self.__transactions.append(f"deposit: +{amount:,}")
        return f"dposit {amount:,} rials done"
