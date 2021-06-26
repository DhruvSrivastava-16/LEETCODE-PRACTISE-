class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        st = 0
        en = len(nums) - 1
        ans = []
        maxs = 0
        
        while st < en:
            ans.append((nums[st],nums[en]))
            if maxs < nums[st] + nums[en]:
                maxs = nums[st] + nums[en]
            st += 1
            en -= 1
            
        return maxs