from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapStore = []
        
        freqMap = Counter(nums)
        
        for key,v in freqMap.items():
            mapStore.append([v,key])
            
        freq = heapq.nlargest(k,mapStore)
        
        return [val[1] for val in freq]
        
        