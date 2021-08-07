class Solution:
    
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i,j in enumerate(nums):
            if i^j!=0:
                return i
            
        return i+1
            
        
            
            
        