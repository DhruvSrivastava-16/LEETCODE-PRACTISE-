from collections import defaultdict, deque

class Solution:
    def dfs(self,graph,root,visited,hasApple):
        visited.add(root)
        
        # if count_a == 0:
            # return 
        
        t_c = 0
        
        
        for n in graph[root]:
            if n not in visited:
                c_c = self.dfs(graph,n,visited,hasApple)
            
                if c_c or hasApple[n]:
                    t_c += c_c + 2
                
        return t_c
    
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        self.steps = 0
        
   
        visited = set()    
        return self.dfs(graph, 0, visited,hasApple)
        
    
        
        
        