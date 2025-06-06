from pymongo import MongoClient

class MongoDatabase:
    instance = None
    @classmethod
    def __new__(cls, *args):
        
        if cls.instance is None:
            cls.instance = super().__new__(*args)
        return cls.instance
    
    def __init__(self):
        self.client = MongoClient()
        self.database = self.client['crawler']
    


