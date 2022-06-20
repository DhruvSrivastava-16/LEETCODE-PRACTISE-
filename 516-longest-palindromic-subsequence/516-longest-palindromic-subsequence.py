class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        
        string2 = s[::-1]
        dp = [[0 for i in range(len(s)+1)] for j in range(len(string2)+1)]
        ans = ''
        
        for i in range(1,len(string2)+1):
            for j in range(1,len(s)+1):
                
                if string2[i-1] == s[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                    
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                  
        return dp[-1][-1]