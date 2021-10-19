class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        currentSum = 0
        d = dict()
        for i, s in enumerate([0] + nums):
            currentSum += s
            modk = currentSum % k
            if modk in d: 
                if i - d[modk] >= 2:
                    return True
            else:
                d[modk] = i
            
        return False
        
            
        
        