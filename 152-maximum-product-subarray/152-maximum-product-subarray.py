class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxSoFar = nums[0]
        minSoFar = nums[0]
        result = nums[0]
        
        for i in range(1,len(nums)):
            
            temp = max(nums[i],nums[i]*maxSoFar,nums[i]*minSoFar)
            minSoFar = min(nums[i],nums[i]*maxSoFar,nums[i]*minSoFar)
            
            maxSoFar = temp
            
            result = max(maxSoFar,result)
            
        return result