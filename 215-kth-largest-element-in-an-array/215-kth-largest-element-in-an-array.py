import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        maxNums = [-num for num in nums]
        
        # heapq.heapify(maxNums)
        
        return -heapq.nsmallest(k,maxNums)[-1]