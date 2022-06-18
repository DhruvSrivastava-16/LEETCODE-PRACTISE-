class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        
        total = sum(nums)
        
        if total%2!=0:
            return False
        
        mid = total//2
        dp = [[False for j in range(mid+1)] for i in range(len(nums)+1)]
        
        for j in range(mid+1):
            dp[0][j] = False
        
        for i in range(len(nums)):
            dp[i][0] = True
            
        
        for i in range(1,len(nums)+1):
            for j in range(1,mid+1):
                
                if j<nums[i-1]:
                    dp[i][j] = dp[i-1][j]
                    
                else:
                    
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                    
                    
                    
        return dp[-1][-1]
                    