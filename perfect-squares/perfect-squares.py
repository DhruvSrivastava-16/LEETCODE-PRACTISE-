class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')]*(n+1)
        dp[0]=0
    
        numsquares = [i**2 for i in range(0, int(math.sqrt(n))+1)]
        
        for i in range(1,n+1):
            for sq in numsquares:
                if i<sq:
                    break
                    
                dp[i] = min(dp[i],dp[i-sq]+1)
                
        return dp[-1]
        