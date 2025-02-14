class Manager:
    def __init__(self, _class=None):
        self._class = _class
        
    def __str__(self):
        return f"Manager {self._class}"
    
    def count(self):
        return len(self._class.object_list)
    
    def get(self, **kwargs):
        obj_list = []
        for key, value in kwargs.items():
            for obj in self._class.object_list:
                if hasattr(obj, key) and getattr(obj, key) == value:
                    obj_list.append(obj)
                
        return obj_list
    
    def search(self, **kwargs):
        """_summary_
        :param kwargs:
        :return list
        """
        '''
        area__min = 100
        name = "sara"
        '''
        results = list()
        
        
        for key, value in kwargs.items():
            if key.endswith('__min'):
                key = key[:-5]
                
                compare_key = 'min'
            elif key.endswith('__max'):
                key = key[:-5]
                compare_key = 'max'
            else:
                compare_key = 'equal'
                
            for obj in self._class.object_list:
                if hasattr(obj, key):
                    if compare_key == 'min':
                        result = getattr(obj, key) >= value
                    elif compare_key == 'max':
                        result = getattr(obj, key) <= value
                    else:
                        result = getattr(obj, key) == value
                        
                        
                    if result:
                        results.append(obj)
        return results
                
            
        