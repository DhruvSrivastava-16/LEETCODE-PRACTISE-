class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_pos = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i]>=last_pos:
                last_pos = i
                
        if last_pos==0:
            return True
        
        else:
            return False
            
        