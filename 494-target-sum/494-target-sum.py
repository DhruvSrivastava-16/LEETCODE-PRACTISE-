class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        if (abs(target)+sum(nums))%2!=0:
            return 0
        
        temp = (abs(target)+sum(nums))//2
        
        dp = [[0 for i in range(temp+1)] for j in range(len(nums)+1)]
        
        for j in range(0,temp+1):
            dp[0][j] = 0
            
        for i in range(0,len(nums)+1):
            dp[i][0] = 1
            
        for i in range(1,len(nums)+1):
            for j in range(temp+1): #Important
                
                if nums[i-1]>j:
                    dp[i][j] = dp[i-1][j]
                    
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
         
        print(dp)
        return dp[len(nums)][temp]
                