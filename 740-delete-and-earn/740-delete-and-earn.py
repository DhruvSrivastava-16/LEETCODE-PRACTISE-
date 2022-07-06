from collections import defaultdict
class Solution:
    

        
    
    
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        points = defaultdict(int)
        maxx = -float('inf')
        
        for num in nums:
            points[num] += num
            maxx = max(maxx,num)
            
        @lru_cache
        def maxxScore(num):
            if num == 0:
                return 0

            if num == 1:
                return points[1]

            return max(maxxScore(num-1),maxxScore(num-2) + points[num])
            
        
        return maxxScore(maxx)
            