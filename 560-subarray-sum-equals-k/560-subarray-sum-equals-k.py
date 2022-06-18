from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumMap = defaultdict(int)
        totalCount = 0
        rollingSum = 0
        
        for i in range(0,len(nums)):
            sumMap[rollingSum]+=1
            rollingSum += nums[i]

            if rollingSum-k in sumMap:
                totalCount+=sumMap[rollingSum-k]
        
        return totalCount