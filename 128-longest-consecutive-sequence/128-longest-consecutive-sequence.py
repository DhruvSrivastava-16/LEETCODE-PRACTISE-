class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)
        maxx = 0
        
        for i in seen:
            
            if i-1 not in seen:
                curr = i
                curr_streak = 1
                
                while curr+1 in seen:
                    curr_streak+=1
                    curr+=1
                
                maxx = max(curr_streak,maxx)
            
        return maxx