class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        second = s[::-1]
        dp = [[0 for i in range(len(s)+1)] for j in range(len(s)+1)]
        
        for i in range(1,len(s)+1):
            for j in range(1,len(s)+1):
                
                if s[i-1]==second[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                    
        return dp[-1][-1]