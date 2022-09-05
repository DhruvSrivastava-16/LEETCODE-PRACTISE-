class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        
        values = [future[i]-present[i] for i in range(len(present))]
        
        
        dp = [[0 for i in range(budget+1)] for j in range(len(present)+1)]
        
        for i in range(1,len(dp)):
            for j in range(len(dp[0])):
                
                # if i==0 or j==0:
                #     dp[i][j] = 0
                    
                if present[i-1]<=j:
                    dp[i][j] = max(future[i-1]-present[i-1]+dp[i-1][j-present[i-1]], dp[i-1][j],dp[i-1][j])
                    
                else:
                    dp[i][j] = dp[i-1][j]
        
        # print(dp)
        return dp[-1][-1]
    
#     def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
#         n = len(present)
#         dp = [[0 for i in range(budget+1)] for j in range(n+1)]
        
#         for i in range(1, n+1):
#             for j in range(budget+1):
#                 include = exclude = 0
#                 if j >= present[i-1]:
#                     include = max(future[i-1]-present[i-1]+dp[i-1][j-present[i-1]], dp[i-1][j])
#                 exclude = dp[i-1][j]
#                 dp[i][j] = max(include, exclude)

#         return dp[-1][-1]
                    