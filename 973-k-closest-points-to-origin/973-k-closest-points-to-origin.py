import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dist = []
        for point in points:
            dist.append([point[0]**2+point[1]**2,point])
            
        heapq.heapify(dist)
        
        answer_2d = heapq.nsmallest(k,dist)
        return [i[1] for i in answer_2d ]