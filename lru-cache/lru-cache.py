class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash = {}
        

    def get(self, key: int) -> int:
        
        if key in self.hash:
            t = self.hash[key]
            self.hash.pop(key)
            self.put(key,t)
            return t
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.hash:
            self.hash.pop(key)
            self.put(key,value)
            
            
        elif (len(self.hash)==self.capacity):
            items = list(self.hash.keys())
            self.hash.pop(items[0])
            #print("Now:",self.hash)
            
            self.hash[key] = value
            
        else:
            self.hash[key] = value
            
        #print(self.hash)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)