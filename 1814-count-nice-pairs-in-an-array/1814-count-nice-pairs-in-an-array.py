class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        # nums[i] + rev(nums[j]) == nums[j] + rev(nums[i]) ==> nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
        # counter stores nums[i] - rev(nums[i])
		
        counter = Counter([num - int(str(num)[::-1]) for num in nums])
        return sum([counter[k] * (counter[k] - 1) // 2 for k in counter]) % (10 ** 9 + 7)