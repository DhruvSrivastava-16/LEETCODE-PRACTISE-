import heapq
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq_map = collections.Counter(arr)
        heap = [[v,k] for k,v in freq_map.items()]
        heapq.heapify(heap)
        
        while k>0:
            temp = heapq.heappop(heap)
            if temp[0]>k:
                heap.append(temp[0])
                break
            
            else:
                k = k - temp[0]
                
        return(len(heap))
                
                
        