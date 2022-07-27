class Solution:
    
    def isPoss(self,weights,cap,days):
        
        tempW = 0
        tempD = 1
        
        for w in weights:
            if tempW+w>cap:
                tempD+=1
                tempW = w
                
                
            else:
                tempW+=w
                
        if tempD>days:
            return False
        
        return True
                
                
            
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        ans = float('inf')
        # weights.sort()
        
        minW = max(weights)
        maxW = sum(weights)
        
        while minW<=maxW:
            
            mid = (minW+maxW)//2
            
            if self.isPoss(weights,mid,days):
                ans = min(mid,ans)
                maxW = mid-1
                
            else:
                minW = mid+1
        
        return(ans)