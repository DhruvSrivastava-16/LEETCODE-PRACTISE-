class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 
        
        if len(nums)==1:
            return nums[0]
        
        currSum = nums[0]
        maxSum = currSum
        
        for num in nums[1:]:
            currSum = max(currSum + num, num)
            maxSum = max(currSum, maxSum)
            
        return maxSum
            