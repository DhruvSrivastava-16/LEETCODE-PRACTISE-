class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        heapq.heapify(h)
        
        for i in points:
            d = i[0]**2 + i[1]**2
            p = [d,i]
            heapq.heappush(h,p)
            
        ans = heapq.nsmallest(k,h)
        ans = [i[1] for i in ans]
        return ans
        