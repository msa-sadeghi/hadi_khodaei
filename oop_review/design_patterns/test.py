from abc import ABC, abstractmethod

class Skletone(ABC):
    def __init__(self, size):
        self.size = size
    @abstractmethod   
    def some_method(self):
        pass
        
        
class Body(Skletone):
    def __init__(self, size, some_thing):
        super().__init__(size)
        self.some_thing = some_thing
        
    def some_behavior(self):
        pass
    def some_method(self):
        return super().some_method()
    

s = Body(12, "adasdasd")