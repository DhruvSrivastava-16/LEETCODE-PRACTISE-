class Solution:
    
    def bfs(self,edges,storeMap,node,graph):
        
        dq = deque()
        visited = set()
        
        dq.append((node,0))
        visited.add(node)
        
        while dq:
            
            node, dist = dq.pop()
            storeMap[node]=dist
            
            for ne in graph[node]:
                if ne not in visited:
                    dq.append((ne,dist+1))
                    visited.add(ne)
                    
        return storeMap[node]
        
    def treeDiameter(self, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        storeMap1 = defaultdict(int)
        self.bfs(edges,storeMap1,0,graph)
        
        distMap = list(storeMap1.items())
        distMap.sort(key = lambda x:x[1])
        node2 = distMap[-1][0]
        storeMap2 = defaultdict(int)
        
        self.bfs(edges,storeMap2,node2,graph)
        print(storeMap2)
        return max(storeMap2.values())