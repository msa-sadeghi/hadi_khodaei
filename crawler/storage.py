from abc import ABC, abstractmethod
from mongo import MongoDatabase
import json
class StorageAbstract(ABC):
    @abstractmethod
    def store(self, data, *args):
        pass


class MongoStorage(StorageAbstract):
    def __init__(self):
        self.mongo = MongoDatabase()
    def store(self, data, collection, *args):
       collection = getattr(self.mongo.database, collection)
       print(type(data))
       if isinstance(data, list) and len(data) > 1:
           print(f'Inserted {len(data)} records into {collection}')
           collection.insert_many(data)
       else:
              collection.insert_one(data)

    def load(self, collection, *args):
        collection = getattr(self.mongo.database, collection)
        data = collection.find()
        return data
    def update(self, collection, filter, update, *args):
        collection = getattr(self.mongo.database, collection)
        result = collection.update_one(filter, update)
        return result.modified_count

class FileStorage(StorageAbstract):

    def store(self, data,file, *args):
        with open(f'{file}.json', 'a') as f:
                f.write(json.dumps(data))

