class Solution:
    def valid(self,w,d,cap):
        st = 1
        temp = 0
        print(cap)
        for i in range(0,len(w)):
            temp = temp+w[i]
            if temp>cap:
                st += 1
                temp = w[i]
                
            if st>d:
                print('F',st)
                return False
        print('T',st)    
        return True
        
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        high = sum(weights)
        max_l = -1
        low = 0
        
        for i in weights:
            if max_l<=i:
                max_l = i
                
        low=max_l
        ans = -1
        
        while low<=high:
            mid = (low+high)//2
            if self.valid(weights,days,mid):
                ans = mid
                high = mid - 1
            
            else:
                low = mid + 1
                
        return(ans)
            