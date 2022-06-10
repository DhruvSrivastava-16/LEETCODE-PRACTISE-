from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqMap = Counter(nums)
        ans = list(freqMap.items())
        ans.sort(key = lambda x : x[1])
        return ans[-1][0]
        