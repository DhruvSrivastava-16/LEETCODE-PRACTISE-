from collections import defaultdict

class Solution:
    def f(self):
        return 0
    
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        dict_sum = defaultdict(int)
        r_sum = 0
        dict_sum[r_sum] = 1
        for j in nums:
            
            r_sum+=j
            answer+=dict_sum[r_sum-k]
            dict_sum[r_sum]+=1

        return answer
            
        
            
            