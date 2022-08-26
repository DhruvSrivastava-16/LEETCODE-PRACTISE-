class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        StopBusMap = defaultdict(list)
        
        if source==target:
            return 0
        
        for i in range(len(routes)):
            for j in routes[i]:
                StopBusMap[j].append(i)
        
        graph = defaultdict(set)
        
        for k,v in StopBusMap.items():
            for b in v:
                for i in v:
                    if b!=i:
                        graph[b].add(i)
                
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
            
            
        
            
            
            