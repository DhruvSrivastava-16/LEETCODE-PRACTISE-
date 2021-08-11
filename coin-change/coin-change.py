class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")]*(amount+1)
        if amount==0:
            return 0
      
        dp[0] = 0
        
    
            
       
            
        for i in range(1,amount+1):
            f = 0
            
            for j in coins:
                if i>=j:
                    dp[i] = min(dp[i],dp[i-j]+1)
                        
                    
        if dp[amount]==float("inf"):
            return -1
       
           
        return(dp[amount])
              
        
        