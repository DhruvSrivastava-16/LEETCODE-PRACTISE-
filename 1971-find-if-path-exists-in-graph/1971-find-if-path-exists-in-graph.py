from collections import defaultdict

class Solution:
    def dfsUtil(self,graph ,visited, path, node):
        
        if node not in visited:
            visited.add(node)   
            path.add(node)
            
        for n in graph[node]:
            
            if n not in visited:
                self.dfsUtil(graph, visited, path, n)
            
            
    
    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)
        
        for edge in edges:
            
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        visited = set()
        
        path = set()
        
        self.dfsUtil(graph, visited, path, source)
        
        if destination in path:
            return True
        
        return False
            
        
