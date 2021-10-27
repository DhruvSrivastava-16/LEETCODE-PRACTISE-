import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        mat = []
        for i in range(0,len(arr)):
            mat.append([abs(arr[i]-x),i])
            
        heapq.heapify(mat)
        
        temp = heapq.nsmallest(k,mat)
        ans = []
        for t in temp:
            ans.append(arr[t[1]])
        ans.sort()
        return ans