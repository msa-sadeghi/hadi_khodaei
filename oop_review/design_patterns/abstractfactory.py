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
    pass

class RugsPrice(DetailBase):
    pass


class Rugs(ProductBase):
    def __init__(self, name, price):
        self._name = name
        self._price = price
        
    @property
    def detail(self):
        pass
    @property
    def price(self):
        pass
    
 
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
