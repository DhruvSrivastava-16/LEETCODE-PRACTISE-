class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for amt in range(amount+1)]
        dp[0] = 0
        
        for itr in range(1,amount+1):
            
            for k in coins:
                
                if k<=itr and dp[itr] > dp[itr-k]+1:
                    
                    dp[itr] = 1+dp[itr-k]
                    
        if dp[-1]==float('inf'):
            return -1
        
        else:
            return dp[-1]
                    
                    
            