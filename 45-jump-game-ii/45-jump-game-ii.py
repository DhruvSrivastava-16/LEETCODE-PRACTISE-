class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        # dp[i] means the minimum number of jumps to reach index i
        # for each dp[i]，we need to find the earliest j that can reach i from j
        # dp[i] = dp[j] + 1
        
        dp = [0] * n
        j = 0
        for i in range(1, n):
            while j + nums[j] < i:
                j += 1
            dp[i] = dp[j] + 1
        
        return dp[-1]