class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3: return 0
        diff = sys.maxsize
        nums = sorted(nums)
        for i in range(-1,-4,-1):
            max_num = nums[i] - nums[4+i]
            diff = min(diff,max_num)
        for i in range(3):
            min_num = nums[-4+i] - nums[i]
            diff = min(diff,min_num)
        return diff