from abc import ABC
from manager import Manager
class BaseClass(ABC):
    _id = 0
    object_list = None
    manager = None
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = self.generate_id()
        self.store(self)
        self.set_manager()
        
    
    @classmethod
    def generate_id(cls):
        cls._id += 1
        return cls._id
    
    @classmethod
    def store(cls, obj):
        if cls.object_list is None:
            cls.object_list = list()
        cls.object_list.append(obj)
        
    @classmethod
    def set_manager(cls):
        if cls.manager is None:
            cls.manager = Manager(cls)
            
        
    
    