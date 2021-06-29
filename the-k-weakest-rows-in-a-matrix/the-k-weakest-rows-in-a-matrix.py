class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        h = []
        heapq.heapify(h)
        for i,o in enumerate(mat):
            heapq.heappush(h,[sum(o),i])
            
        
        ans = heapq.nsmallest(k,h)
        ans2 = []
        for i in ans:
            ans2.append(i[1])
            
        return ans2
            