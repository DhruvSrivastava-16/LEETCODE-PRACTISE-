class Solution:
    def minOperations(self, nums: List[int]) -> int:
        l = len(nums)
        tot = 0
        
        for i in range(0,l-1):
            if nums[i+1] - nums[i] <= 0:
                tot = tot + - nums[i+1] + nums[i] + 1
                nums[i+1] = nums[i+1] - nums[i+1] + nums[i] + 1
        print(nums)
                
        return tot
        