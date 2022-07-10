class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        right = 0
        count = 0
        maxCount = 0
        
        while right<len(nums):
            
                
            if nums[left]!=1:
                left+=1
                right = left
                continue
                
            if nums[right]==1:
                right+=1
                maxCount = max(maxCount,right-left)
                continue
                
            else:
                left = right
            
        return maxCount
            
            