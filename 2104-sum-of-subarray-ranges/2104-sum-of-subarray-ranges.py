import heapq

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        sub = []
        minHeap = []
        maxHeap = []
        ans = 0
        
        for i in range(0,len(nums)):
            minHeap = []
            maxHeap = []
            
            heapq.heappush(minHeap,nums[i])
            heapq.heappush(maxHeap,-nums[i])
            
            for j in range(i+1,len(nums)):
                
                heapq.heappush(minHeap,nums[j])
                heapq.heappush(maxHeap,-nums[j])
                
                ans += -maxHeap[0]-minHeap[0]
                
                
                
        return(ans)