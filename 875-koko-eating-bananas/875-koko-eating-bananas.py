import math
class Solution:
    
    def check(self,speed,piles,hr):
        
        total = 0
        if speed == 0:
            return False
        
        for i in range(len(piles)):

            total += math.ceil(piles[i]/speed)
                
        if total<=hr:
            return True
        
        return False
        
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        low = 0
        high = piles[-1]
        answer = 0
        
        while low<=high:
            
            mid = (low+high)//2
            
            if self.check(mid,piles,h):
                answer = mid
                high = mid-1
                
            else:
                low = mid+1
            
        return answer