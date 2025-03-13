
COUNTRIES = ['Italy', 'USA']
COUNTRY_CODE = {
    'Italy': 10,
    'USA' : 20

}
class User:
    pass


class Address:
    def __init__(self, country):
        self.country = country

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Purchase:
    def __init__(self, user, address):
        self.user = user
        self.address = address
        self.product_list = []

    def add_products(self, products_list):
        if not isinstance(products_list, list):
            products_list = [products_list]
        self.product_list.extend(products_list)

    def total_price(self):
        s = 0
        for product in self.product_list:
            s += product.price

        return s
    
def calculate_something(func):
    def wrapped_func(pur):
        code = COUNTRY_CODE[pur.address.country]
        total_price = pur.total_price()
        return total_price + total_price * code / 100
    return wrapped_func


def show_total_price(p):
    return p.total_price()

@calculate_something
def show_another_total_price(p):
    return p.total_price()

if __name__ == "__main__":
    user = User()
    italy_address = Address(country=COUNTRIES[0])
    usa_address = Address(country=COUNTRIES[1])

    p1 = Product('p1', 100)
    p2 = Product('p2', 200)
    p3 = Product('p3', 300)
    p4 = Product('p4', 250)

    products = [p1, p2, p3, p4]

    purchase_italy = Purchase(user, address=italy_address)
    purchase_italy.add_products(p1)
    purchase_italy.add_products([p2,p3])
    print(show_total_price(purchase_italy))
    print(show_another_total_price(purchase_italy))

