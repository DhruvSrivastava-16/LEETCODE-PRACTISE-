class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        dp = [float('inf') for i in range(amount+1)]
        dp[0] = float('inf')
        
        for c in coins:
            if c<=amount:
                dp[c] = 1
        
        for i in range(1,len(dp)):
            
            for c in range(len(coins)):
                if i-coins[c]>=0:
                
                    dp[i] = min(dp[i],dp[i-coins[c]]+1)
        
        print(dp)
        if dp[-1] == float('inf'):
            return -1
        
        return(dp[-1])
                
                