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
# from collections import Counter

# def bucket_minute(timestamps):
#     for ts in timestamps:
#         yield ts[:16]  # فرض: فرمت ISO مانند 2025-11-07T09:37

# def count_by_minute(minutes):
#     counts = Counter()
#     for m in  minutes:
#         counts[m] += 1
#     return counts



# class User:
#     # Class variable - مشترک بین همه instances
#     user_count = 0
    
#     def __init__(self, username, email):
#         # Instance variables - منحصر به هر object
#         self.username = username
#         self.email = email
#         self.is_active = True
#         User.user_count += 1
    
#     def __str__(self):
#         return f"User: {self.username}"
    
#     def __repr__(self):
#         return f"User(username='{self.username}', email='{self.email}')"
    
#     def activate(self):
#         self.is_active = True
#         return f"{self.username} activated"
    
#     def deactivate(self):
#         self.is_active = False
#         return f"{self.username} deactivated"

# # استفاده
# user1 = User("john_doe", "john@example.com")
# user2 = User("jane_doe", "jane@example.com")

# print(User.user_count)  # 2
# print(user1)  # User: john_doe


# class BlogPost:
#     def __init__(self, title, content):
#         self._title = title
#         self._content = content
#         self._views = 0
    
#     @property
#     def title(self):
#         """Getter برای title"""
#         return self._title
    
#     @title.setter
#     def title(self, value):
#         """Setter با validation"""
#         if len(value) < 5:
#             raise ValueError("Title must be at least 5 characters")
#         self._title = value
    
#     @property
#     def views(self):
#         return self._views
    
#     @property
#     def is_popular(self):
#         """Computed property"""
#         return self._views > 1000
    
#     def increment_views(self):
#         self._views += 1

# # استفاده
# post = BlogPost("Django Tutorial", "Content here...")
# post._views = -100
# print(post.title)  # Django Tutorial
# post.title = "Advanced Django"  # استفاده از setter
# print(post.is_popular)  # False
# print(post.views)  # False



# from datetime import datetime

# class Article:
#     article_count = 0
    
#     def __init__(self, title, author, published_date):
#         self.title = title
#         self.author = author
#         self.published_date = published_date
#         Article.article_count += 1
    
#     @classmethod
#     def create_draft(cls, title, author):
#         """Factory method برای ساخت draft"""
#         return cls(title, author, None)
    
#     @classmethod
#     def from_dict(cls, data):
#         """ساخت object از dictionary"""
#         return cls(
#             title=data['title'],
#             author=data['author'],
#             published_date=data.get('published_date')
#         )
    
#     @staticmethod
#     def is_valid_date(date_string):
#         """Utility method - نیازی به instance یا class ندارد"""
#         try:
#             datetime.strptime(date_string, '%Y-%m-%d')
#             return True
#         except ValueError:
#             return False
    
#     @classmethod
#     def get_count(cls):
#         return cls.article_count

# # استفاده
# article1 = Article("Django Guide", "John", "2025-10-01")
# print(article1.is_valid_date("2025-10-01"))
# article2 = Article.create_draft("New Post", "Jane")
# print(article2.is_valid_date("2025-10-01"))
# data = {'title': 'Python Tips', 'author': 'Ali'}
# article3 = Article.from_dict(data)

# print(Article.is_valid_date("2025-10-01"))  # True
# print(Article.get_count())  # 3



# class NotificationService:
#     def send(self, recipient, message):
#         raise NotImplementedError("Subclass must implement send()")

# class EmailNotification(NotificationService):
#     def send(self, recipient, message):
#         return f"Email sent to {recipient}: {message}"

# class SMSNotification(NotificationService):
#     def send(self, recipient, message):
#         return f"SMS sent to {recipient}: {message}"

# class PushNotification(NotificationService):
#     def send(self, recipient, message):
#         return f"Push notification sent to {recipient}: {message}"

# class NotificationManager:
#     def __init__(self):
#         self.services = []
    
#     def add_service(self, service):
#         self.services.append(service)
    
#     def notify_all(self, recipient, message):
#         """Polymorphism در عمل"""
#         results = []
#         for service in self.services:
#             # هر service متد send خود را دارد
#             results.append(service.send(recipient, message))
#         return results

# # استفاده
# manager = NotificationManager()
# manager.add_service(EmailNotification())
# manager.add_service(SMSNotification())
# manager.add_service(PushNotification())

# results = manager.notify_all("user@example.com", "Welcome!")
# for result in results:
#     print(result)


# class JSONSerializer:
#     def serialize(self, data):
#         import json
#         return json.dumps(data)

# class XMLSerializer:
#     def serialize(self, data):
#         # ساده‌سازی شده
#         return f"<data>{data}</data>"

# class YAMLSerializer:
#     def serialize(self, data):
#         # ساده‌سازی شده
#         return f"---\ndata: {data}"

# def save_data(data, serializer):
#     """
#     Duck typing: اگر serializer متد serialize دارد، کار می‌کند
#     نیازی به وراثت یا interface خاص نیست
#     """
#     serialized = serializer.serialize(data)
#     print(f"Saving: {serialized}")
#     return serialized

# # استفاده
# data = {'user': 'john', 'age': 30}

# save_data(data, JSONSerializer())
# save_data(data, XMLSerializer())
# save_data(data, YAMLSerializer())




class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Overload + operator"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Overload - operator"""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """Overload * operator"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __eq__(self, other):
        """Overload == operator"""
        return self.x == other.x and self.y == other.y
    
    def __len__(self):
        """برای len()"""
        import math
        return int(math.sqrt(self.x**2 + self.y**2))

# استفاده
v1 = Vector(3, 4)
v2 = Vector(1, 2)

v3 = v1 + v2
print(v3)  # Vector(4, 6)

v4 = v1 * 2
print(v4)  # Vector(6, 8)

print(len(v1))  # 5
