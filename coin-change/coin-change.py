class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for i in range(amount+1)]
        if amount == 0:
            return 0
        
        dp[0] = 0
        
        for i in range(1,amount+1):
            
            for k in coins:
                if i-k>=0 and dp[i]>1+dp[i-k]:
                    dp[i] = 1+dp[i-k]
                    
        
        if dp[amount] == float('inf'):
            return -1
        
        return dp[amount]
        