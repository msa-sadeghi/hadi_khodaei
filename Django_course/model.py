# import json

# class User:
#     def __init__(self, username, email):
#         self.username = username
#         self.email =  email
#         self.is_active = True

#     def deactivate(self):
#         self.is_active = False
#         print(f"{self.username} deactived.")

#     def get_info(self):
#         return f"username: {self.username}, email :{self.email}"
    
# class Product:
#     total_products = 0
#     def __init__(self,name, price, category, stock=0):
#         self.id = Product.total_products + 1
#         self.name = name
#         self.price = price
#         self.category = category
#         self.stock = stock
#         Product.total_products += 1

#     def is_available(self):
#         return self.stock > 0
    
#     def sell(self, quantity = 1):
#         if quantity > self.stock:
#             return {"success": False, "message": "not exists in stock"}
#         self.stock -= quantity
#         total_price = self.price * quantity
#         return {
#             "success" : True,
#             "message" : f"{quantity} number {self.name} selled",
#             "total" : total_price
#         }
#     def __str__(self):
#         return f"id:{self.id}, name:{self.name}"
#     def __repr__(self):
#         return f"id:{self.id}, name:{self.name}"
    

# products = []
# for i in range(3):
#     p = Product("lap", "100", "elec", 1)
#     temp = {
#         'id':p.id,
#         'name' : p.name
#     }
#     products.append(temp)

# # with open("products.json", "w", encoding = "utf-8") as f:
# #     json.dump(products, f, indent=2)
# with open("products.json", "r", encoding = "utf-8") as f:
#     print(json.load(f)[0]['id'])



# class BankAccount:
#     def __init__(self, owner, initial_balance=0):
#         self.owner = owner
#         self.__balance= initial_balance
#         self.__transactions = []

#     def deposit(self, amount):
#         if amount <= 0:
#             return "you cant deposit 0"
#         self.__balance += amount
#         self.__transactions.append(f"deposit: +{amount:,}")
#         return f"dposit {amount:,} rials done"



# def apply_operation(func, x,y):
#     return func(x,y)

# def add(x,y):
#     return x + y
# def mul(x,y):
#     return x * y

# result1 = apply_operation(add, 5,3)

# print(result1)

# def validate_field(value, validators):
#     for validator in validators:
#         if not validator(value):
#             return False
#     return True


# is_positive = lambda x : x > 0
# is_even = lambda x : x % 2 == 0

# print(validate_field(5, [is_positive, is_even]))

# def repeat(times):
#     def timer_decorator(func):
#         import time
#         def wrapper(*args , **kwargs):
#             start = time.time()
#             for i in range(2):
#                 result = func(*args, **kwargs)
#             end = time.time()
#             print(f"{func.__name__} took {end - start:.2f} seconds")
#             return result
#         return wrapper
#     return timer_decorator

# @repeat(times=22)
# def slow_function():
#     import time
#     time.sleep(2)
#     return "Done"


# print(slow_function())


# def count_up_to(n):
#     count = 1
#     while count <= n:
#         yield count
#         count += 1

# counter = count_up_to(5)
# print(next(counter))
# print(next(counter))
# import pandas as pd
# def iter_trades(chunck=1):
#     for df in pd.read_csv("test.csv", chunksize=chunck):
        
#         filt = df[df['Price'] >= 1000] 
#         yield filt
#     # return None

# for tr in iter_trades():
#     print(tr)


# squares_list = (x**2 for x in range(1_000_000))
# print(next(squares_list))
# print(next(squares_list))
# print(next(squares_list))
# print(next(squares_list))

# def read_logs(filename, encoding='utf-8'):
#     with open(filename, encoding=encoding) as f:
#         for line in f:
#             yield line

# def filter_errors(lines, keyword="ERROR"):
#     for line in lines:
#         if keyword in line:
#             yield line

# def extract_timestamp(lines):
#     for line in lines:
#         # استخراج timestamp
#         yield line.split()[0]

# # Pipeline
# logs = read_logs('app.log')
# errors = filter_errors(logs)
# for ts in extract_timestamp(errors):
#     print(ts)
from collections import Counter

def bucket_minute(timestamps):
    for ts in timestamps:
        yield ts[:16]  # فرض: فرمت ISO مانند 2025-11-07T09:37

def count_by_minute(minutes):
    counts = Counter()
    for m in  minutes:
        counts[m] += 1
    return counts

