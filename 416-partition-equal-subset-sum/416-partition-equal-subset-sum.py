class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        totalSum = sum(nums)
        
        if totalSum%2!=0:
            return False
        
        totalSum //=2
        
        
        dp = [[False for j in range(0,totalSum+1)] for i in range(len(nums)+1)]
        
        for i in range(0,len(nums)+1):
            dp[i][0] = True
            
        for i in range(1,totalSum+1):
            dp[0][i] = False
            
        for i in range(1,len(nums)+1):
            for j in range(1,totalSum+1):
                
                if nums[i-1]>j:
                    dp[i][j] = dp[i-1][j]
                    
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                    
        return dp[-1][-1]
        