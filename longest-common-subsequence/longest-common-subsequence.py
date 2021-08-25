class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len_x = len(text1)
        len_y = len(text2)


        dp = [[0 for j in range(0,len_y+1)] for i in range(0,len_x+1)]



        for i in range(1,len_x+1):
            for j in range(1,len_y+1):

                if text1[i-1] == text2[j-1]:

                    dp[i][j] = 1 + dp[i-1][j-1]

                else:

                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])


        return(dp[len_x][len_y])