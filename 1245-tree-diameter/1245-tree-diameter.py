from collections import deque,defaultdict
class Solution:
    def bfs(self,node,graph):
        dq = deque()
        visited = set()
        visited.add(node)
        dist = 0
        dq.append((node,0))
        distMap = defaultdict(int)
        while dq:
            
            node, dist = dq.popleft()
            distMap[node] = dist
            
            for n in graph[node]:
                if n not in visited:
                    dq.append((n,dist+1))
                    visited.add(n)
                    
        return distMap
    
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        distMap = self.bfs(0,graph)
        distList = list(distMap.items())
        distList.sort(key = lambda x:x[1])
        node = distList[-1][0]
        
        distMap2 = self.bfs(node,graph)
        distMapList = list(distMap2.items())
        distMapList.sort(key = lambda x:x[1])
        return distMapList[-1][1]
        