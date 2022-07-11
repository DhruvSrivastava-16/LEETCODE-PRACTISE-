class Solution:
    def mincostTickets(self, days: List[int], cost: List[int]) -> int:
        n = len(days)
        dp = [0 for i in range(days[-1]+1)]
        
        
        for i in range(1,len(dp)):
            if i in days:
                dp[i] = min(dp[i-1]+cost[0],dp[max(i-7,0)]+cost[1],dp[max(i-30,0)]+cost[2])
            else:
                dp[i] = dp[i-1]
        
        print(dp)
        return dp[-1]