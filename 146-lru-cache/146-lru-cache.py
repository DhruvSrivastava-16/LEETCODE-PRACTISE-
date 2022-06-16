class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.hmap = {}

    def get(self, key: int) -> int:
        if key in self.hmap:
            val = self.hmap.pop(key)
            self.hmap[key] = val
            
            return val
        
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.hmap:
            valueOld = self.hmap.pop(key)
            self.put(key,value)
            
        elif len(self.hmap) == self.capacity:
            remove = list(self.hmap.keys())[0]
            self.hmap.pop(remove)
            self.hmap[key] = value
        
        else:
            self.hmap[key] = value
            
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)