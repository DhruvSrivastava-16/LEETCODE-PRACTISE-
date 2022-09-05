class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        
        pq = []
        currFuel = startFuel
        currLocation = 0
        prev = 0
        count = 0
        
        stations.append((target, float('inf')))
        
        for location,capacity in stations:
            
            currFuel -= location-prev
            
            while pq and currFuel<0:
                currFuel += -heapq.heappop(pq)
                count+=1
            
            if currFuel<0:
                return -1
            
            heapq.heappush(pq,-capacity)
            prev = location
        

        return count
        