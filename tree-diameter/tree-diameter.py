class Solution:
    def dfs(self,graph,visited,root):
        visited.add(root)
        d_1 = 0
        d_2 = 0
        
        temp_dist = 0
        
        for n in graph[root]:
            if n not in visited:
                temp_dist = 1 + self.dfs(graph,visited,n)
                
            if temp_dist>d_1:
                d_1, d_2 = temp_dist, d_1
         
                
            elif temp_dist>d_2:
                d_2 = temp_dist
                
        self.diameter = max(self.diameter,d_1+d_2)
            
        return d_1
    
    def treeDiameter(self, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
            
        visited = set()
        
        self.diameter = 0
        self.dfs(graph,visited,0)
        return self.diameter