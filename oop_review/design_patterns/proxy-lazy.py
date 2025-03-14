from time import sleep

class MySQLHandler:
    def __init__(self):
        sleep(1)

    def connect(self):
        return "Connection to the mysql stablished!!!"
class MongoHandler:
    def __init__(self):
        sleep(50)

    def connect(self):
        return "Connection to the Mongo stablished!!!"
    
class LazyLoader:
    def __init__(self, cls):
        self.cls = cls
        self.object = None

    def __getattr__(self, item):
        if self.object is None:
            self.object = self.cls()
        return getattr(self.object, item)
    
if __name__ == "__main__":
    mysql = LazyLoader(MySQLHandler)
    print(mysql.connect())
    mongo = LazyLoader(MongoHandler)
    print(mongo.connect())


# https://refactoring.guru/design-patterns/proxy
# https://www.geeksforgeeks.org/lazy-loading-design-pattern/