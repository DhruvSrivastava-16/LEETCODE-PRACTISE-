class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for i in range(0,n+1)]
        
        
        for i in range(0,n+1):
            if i == 0:
                dp[i] = 0
            elif i == 1:
                dp[i] = 1
                
            elif i == 2:
                dp[i] = 2
            else:
                dp[i] = dp[i-1]+dp[i-2]
            
            
        return dp[-1]