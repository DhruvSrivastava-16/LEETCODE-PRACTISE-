class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = [[0 for i in range(len(word1)+1)] for j in range(len(word2)+1)]
        
        for i in range(len(word1)+1):
            dp[0][i] = i
            
        for j in range(len(word2)+1):
            dp[j][0] = j
        
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
            
                left = dp[i][j-1]
                up = dp[i-1][j]
                leftUp = dp[i-1][j-1]
                           
                if word1[j-1]==word2[i-1]:
                
                    dp[i][j] = 1+min(left,up,leftUp-1)
                           
                else:
                    dp[i][j] = 1+min(left,up,leftUp)
                           
        return dp[-1][-1]