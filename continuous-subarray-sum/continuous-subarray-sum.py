class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        
        r_sum = 0
        h_map = {}
        nums = [0] + nums
        
        for i in range(0,len(nums)):
            
            r_sum += nums[i]
            r_mod = r_sum%k 
            
            if r_mod in h_map:
                
                if i-h_map[r_mod]>=2:
                    return True
                
            else:
                
                h_map[r_mod]  = i
        
        
        return False