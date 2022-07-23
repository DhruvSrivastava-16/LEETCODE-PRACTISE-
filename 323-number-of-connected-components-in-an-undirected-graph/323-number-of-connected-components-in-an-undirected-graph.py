class Solution:
    
    def dfs(self,node,visited):
        global graph
        
        visited.add(node)
        
        for ne in graph[node]:
            if ne not in visited:
                self.dfs(ne,visited)
                
                
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        global graph
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
            
        visited = set()
        components = 0
        
        for node in range(n):
            
            if node not in visited:
                components+=1
                self.dfs(node,visited)
                
        return components