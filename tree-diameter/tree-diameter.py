from collections import defaultdict

diameter = 0
class Solution:
    def helper(self,graph,visited,root):
        global diameter
        
        visited.add(root)
        d1 = 0
        d2 = 0
        l = 0
        
        for n in graph[root]:
            if n not in visited:
                l = 1 + self.helper(graph,visited,n)
                
            if l>d1:
                d1, d2 = l, d1
                
            elif l>d2:
                d2 = l
                
        diameter = max(diameter,d1+d2)
        
        return d1
        
    
    def treeDiameter(self, edges: List[List[int]]) -> int:
        
        global diameter
        graph = defaultdict(list)
        
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
            
        visited = set()
        
        diameter = 0
        self.helper(graph,visited,0)
        return diameter