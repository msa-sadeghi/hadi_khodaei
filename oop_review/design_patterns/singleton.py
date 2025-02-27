class Singletone:
    @classmethod
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(*args, **kwargs)
        return cls.instance
    
class DataBaseHandler(Singletone)  :
    pass      
        
    
        
s1 = Singletone()
print(id(s1))
s2 = DataBaseHandler()
print(id(s2))
s3 = Singletone()
print(id(s3))
print(id(s1) == id(s2) == id(s3))