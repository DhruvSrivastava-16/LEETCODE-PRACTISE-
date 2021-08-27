from collections import defaultdict

class Solution:
    def f(self):
        return 0
    
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        dict_sum = defaultdict(self.f)
        temp_sum = 0
        dict_sum[temp_sum] +=1
        for j in nums:
            
            temp_sum += j
            
            answer = answer + dict_sum[temp_sum-k]
            dict_sum[temp_sum]+=1
            
        return(answer)
            
            