class HitCounter:

    def __init__(self):
        self.mapStore = defaultdict(list)

    def hit(self, timestamp: int) -> None:
        self.mapStore[timestamp].append(1)
        return None
        

    def getHits(self, timestamp: int) -> int:
        keys = sorted(list(self.mapStore.keys()))
        
        latest = timestamp
        og = timestamp
        itr = 1
        total = 0
        
        while itr<=300:
            
            if latest not in self.mapStore:
                latest = og - itr
                itr+=1
                continue
            total += len(self.mapStore[latest])
            latest = og - itr
            itr+=1
        
        
            

            
        return total
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)