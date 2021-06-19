class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        h = {}
        gp = 0
        
        for i in range(0,len(nums)):
            
            if nums[i] in h:
                h[nums[i]] = h[nums[i]] + 1
                
                
            
            else:
                h[nums[i]] = 1
                
        for i in h:
            gp = gp + sum([k for k in range(1,h[i])])
      
                
        return gp