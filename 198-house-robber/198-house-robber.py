class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums)+1)]
        dp[-1], dp[-2] = 0, nums[-1]
        
        for i in range(len(nums)-2,-1,-1):
            
            dp[i] = max(dp[i+2] + nums[i],dp[i+1])
            
        return (dp[0])