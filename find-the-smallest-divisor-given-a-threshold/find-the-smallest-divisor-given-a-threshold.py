import math
class Solution:
    def check(self,dv,nums):
        ans = 0
        for i in nums:
            ans += math.ceil(i/dv)
        return ans
    
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        low = 1
        high = max(nums)+1
        
        while low<high:
            
            mid = (low+high)//2
            test = self.check(mid,nums)
            
            if test<=threshold:
                ans = mid
                high = mid
                
            else:
                low = mid+1
                
                
        return ans
            