class Solution:
    
    def isPoss(self,mid,time,totalTrips):
        total = 0
        for i in range(len(time)):
            total += int(mid/time[i])
        return total>=totalTrips
            
            
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        total = 0
        currTotal = 0
        clock = 0
        time.sort()
        
        right = time[-1]*totalTrips
        left = 0
        ans = []
        
        while left<=right:
            
            mid = (left+right)//2
            if self.isPoss(mid,time,totalTrips):
                ans = (mid)
                right = mid-1
                
            else:
                left = mid+1
                
        return (ans)
                
            
            
        
            
            