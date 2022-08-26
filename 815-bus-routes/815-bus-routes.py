class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        if source == target:
            return 0
        
        StopBusMap = defaultdict(list)
        
        for bus in range(len(routes)):
            for stop in routes[bus]:    
                StopBusMap[stop].append(bus)
                
                
        graph = defaultdict(set)
        
        for key, value in StopBusMap.items():
            
            for itr1 in value:
                
                for itr2 in value:
                    
                    if itr1!=itr2:
                        
                        graph[itr1].add(itr2)
        
        print(graph)

                
        answer = float('inf')
        
        for node in StopBusMap[source]:
            dq = deque()
            dist = 1
            visit = set()
            dq.append((node,dist))
            visit.add(node)
            
            while dq:
                
                node, dist = dq.pop()
                if node in StopBusMap[target]:
                    answer = min(dist,answer)
                
                for ne in graph[node]:
                    
                    if ne in StopBusMap[target]:
                        answer = min(answer,dist+1)
                        
                    if ne not in visit:
                        visit.add(ne)
                        dq.append((ne,dist+1))
                        
        if answer==float('inf'):
            return -1
        
        return answer
            
            
        
            
            
            