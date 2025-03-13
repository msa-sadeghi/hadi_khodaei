from abc import ABC, abstractmethod

class ProductBase(ABC):
    @abstractmethod
    def detail(self):
        pass
    @abstractmethod
    def price(self):
        pass

class DetailBase(ABC):
    @abstractmethod
    def show(self):
        pass
class RugsDetail(DetailBase):
    def __init__(self, rugs):
        self.rugs = rugs
    
    def show(self):
        return f"rugs detail: {self.rugs._name}"

class RugsPrice(DetailBase):
    def __init__(self, rugs):
        self.rugs = rugs
    
    def show(self):
        return f"rugs detail: {self.rugs._price}"


class Rugs(ProductBase):
    def __init__(self, name, price):
        self._name = name
        self._price = price
        
    @property
    def detail(self):
        return RugsDetail(self)
    @property
    def price(self):
        return RugsPrice(self)
    
 
def Mobile(ProductBase):
    def __init__(self, name, price, model):
        self._name = name
        self._price = price
        self._model = model
    @property
    def detail(self):
        pass
    @property
    def price(self):
        pass



if __name__ == '__main__':
    r1 = Rugs("Persian rugs1", 3000)
    r2 = Rugs("Persian rugs2", 6000)

    for product in [r1, r2]:
        print(product.detail.show())
        print(product.price.show())