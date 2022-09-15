class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        total = len(arr)
        answer = 0
        cmap = Counter(arr)
        heap = []
        
        for key in cmap.keys():
            heapq.heappush(heap,(-cmap[key],key))
            
        while heap:
            rem, key = heapq.heappop(heap)
            
            total+=rem
            print(total,rem,key)
            answer+=1
            if total<=len(arr)//2:
                return answer
            
            
        return answer