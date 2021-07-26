class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for i in nums:
            if i not in dict1:
                dict1[i] = 1
                
            else:
                dict1[i] += 1
                
        
        heap = []
        for i in dict1.keys():
            heap.append([-dict1[i],i])
            
        
        heapq.heapify(heap)
        ans = []
        
        for i in range(0,k):
            k = heapq.heappop(heap)
            ans.append(k[1])
            
        return(ans)
        
        