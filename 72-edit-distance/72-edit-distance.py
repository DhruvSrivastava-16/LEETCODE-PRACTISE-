class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m = len(word1)
        n = len(word2)
        
        if m*n == 0:
            return m+n
        
        
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        
        for i in range(0,m+1):
            dp[0][i] = i
            
        for j in range(0,n+1):
            dp[j][0] = j
            
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                
                left = dp[i][j-1]
                down = dp[i-1][j]
                leftDown = dp[i-1][j-1]
                if word1[j-1]!=word2[i-1]:    
                    dp[i][j] = 1+min(left,down, leftDown)
                    
                else:
                    dp[i][j]  = min(leftDown,1+min(left,down))
                
        return dp[-1][-1]