class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [[0 for i in range(n+1)] for j in range(n+1) ]
        
        for i in range(0,len(dp)):
            for j in range(0,len(dp[0])):
                
                if i==0 or j==0:
                    dp[i][j] = 1
                    
                    
        for i in range(1,len(dp)):
            for j in range(1,len(dp)):
                
                if i>=j:
                    
                    dp[i][j] = max(dp[i-j][j]*j,dp[i][j-1])
                    
                else:
                    dp[i][j] = dp[i][j-1]
                    
                    
        return dp[n][n-1]
                    
                    
                