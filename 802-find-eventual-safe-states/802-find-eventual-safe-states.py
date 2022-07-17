def retFalse():
    return False

class Solution:

    
    def dfs(self,graph,node):
        
        visited.add(node)
        self.stk[node]=True

        
        for ne in graph[node]:
            
            if ne not in visited:
                if self.dfs(graph,ne):
                    return True
                
            elif self.stk[ne]==True:
                self.cycle = True
                return True
            
                
        self.stk[node]=False
        return False
        
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        nodes = len(graph)
        global visited
        visited = set()
        self.stk = defaultdict(retFalse)
        self.cycle = False
        answer = []
        self.globalVisited = set()
        
        for n in range(nodes):
            if not self.dfs(graph,n):
                    answer.append(n)

            
                
        return answer
            
            
            