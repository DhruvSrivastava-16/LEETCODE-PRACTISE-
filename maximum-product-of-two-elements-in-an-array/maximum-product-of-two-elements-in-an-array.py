
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        h = []
        heapq.heapify(h)
        for i in nums:
            heapq.heappush(h,-i)
            
        a = heapq.heappop(h)
        b = heapq.heappop(h)
        
        return (a+1)*(b+1)
        