from collections import defaultdict

class Solution:
    
    def Cyclic(self,n, graph, recStack, visited):
        
        visited.add(n)
        recStack[n] = True
        
        for neighbour in graph[n]:
            
            if neighbour not in visited:
                
                if self.Cyclic(neighbour, graph, recStack, visited):
                    return True
                
            elif recStack[neighbour] == True:
                    return True
        
        recStack[n] = False
        return False
        
                
    def canFinish(self, numCourse: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        recStack = {i : False for i in range(numCourse)}
        
        for pre in prerequisites:
            
            graph[pre[1]].append(pre[0])
            
        visited = set()
        
        
        for n in range(numCourse):
            if n not in visited:
                if self.Cyclic(n, graph, recStack, visited):
                    return False
                
        return True
    