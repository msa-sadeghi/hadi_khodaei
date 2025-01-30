from abc import ABC, abstractmethod

class Apartment:
    def __init__(self, floor, elevator, *args, **kwargs):
        self.floor = floor 
        self.elevator = elevator
        
class House:
    def __init__(self, age, address, *args, **kwargs):
        self.age = age
        self.address = address
        
        
class Rent(ABC):
    def __init__(self, fixed_amount, monthly_amount):
        self.fixed_amount = fixed_amount
        self.monthly_amount = monthly_amount
    @abstractmethod   
    def show_banner(self):
        pass
        
class Sale(ABC):
    def __init__(self, fee):
        self.fee = fee
    @abstractmethod
    def show_banner(self):
        pass
        
        
class ApartmentRent(Apartment, Rent):
    def __str__(self):
        return f"{self.floor}, {self.fixed_amount}"
    def show_banner(self):
        return "show banner"
class ApartmentSale(Apartment, Sale):
    def __str__(self):
        return f"{self.floor}, {self.fee}"
    def show_banner(self):
        return "show banner"
        
        
class HouseRent(House, Rent):
    def __str__(self):
        return f"{self.floor}, {self.fixed_amount}"
    def show_banner(self):
        return "show banner"
class HouseSale(House, Sale):
    def __str__(self):
        return f"{self.floor}, {self.fee}"
    def show_banner(self):
        return "show banner"
    
    
if __name__ == "__main__":
    estates = list()
    apartment_rent = ApartmentRent(floor=2, elevator=True, fixed_amount=12, monthly_amount = 1)
    estates.append(apartment_rent)
    
    apartment_sale = ApartmentSale(floor = 2, elevator=True, fee=200)
    estates.append(apartment_sale)
    
    house_rent = HouseRent(age=4, address="teh", fixed_amount = 12, monthly_amount = 2)
    estates.append(house_rent)
    
    house_sale = HouseSale(age=5, address="teh", fee="340")
    estates.append(house_sale)
    
    for estate in estates:
        print(estate.show_banner())