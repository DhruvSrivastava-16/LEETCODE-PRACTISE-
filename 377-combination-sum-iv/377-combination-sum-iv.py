class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = [0 for i in range(target+1)]
        dp[0] = 1
        
        for cm in range(target+1):
            
            for num in nums:
                
                if cm>=num:
                    
                    dp[cm] += dp[cm-num]
                    
        return dp[target]