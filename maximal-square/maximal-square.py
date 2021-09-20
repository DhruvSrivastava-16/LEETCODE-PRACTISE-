class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        dp = [[0 for i in range(0,len(matrix[0])+1)] for i in range(len(matrix)+1)]
        maxx = 0
        for j in range(1,len(matrix[0])+1):
            for i in range(1,len(matrix)+1):
                
                if matrix[i-1][j-1]=='1':
                    
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    maxx = max(maxx,dp[i][j])
        
        return(maxx*maxx)