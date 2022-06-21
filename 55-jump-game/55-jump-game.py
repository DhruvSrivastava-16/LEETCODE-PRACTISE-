class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        lastP = len(nums)-1
        
        for i in range(len(nums)-1,-1,-1):
            
            if lastP-i<=nums[i]:
                lastP = i
                
        if lastP == 0:
            return True
        
        return False