class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        curr_sum = 0
        max_sum = -10000
        
        for i in range(0,len(nums)):
            
            
            curr_sum = max(curr_sum+nums[i],nums[i])
            
            if curr_sum>max_sum:
                max_sum = curr_sum
                
        return max_sum