class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    
   

        graph = defaultdict(dict)
        for time in times:
            graph[time[0]][time[1]] = time[2]
            
        heap = []
        distance = {i:float('inf') for i in range(1,n+1)}
        distance[k] = 0
        
        heapq.heappush(heap,(0,k))
        
        while heap:
            
            dist, node = heapq.heappop(heap)
            
            for ne, weight in graph[node].items():
                
                if dist + weight < distance[ne]:
                    
                    distance[ne] = dist + weight
                    heapq.heappush(heap,(distance[ne],ne))
                    
        ans =  max(distance.values())
        
        if ans == float('inf'):
            return -1
        
        return ans
            
        