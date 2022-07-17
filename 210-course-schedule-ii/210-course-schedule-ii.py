class Solution:
    
    def dfs(self,node,visited,graph,top):
        visited.add(node)
        self.recStack[node] = True
        for ne in graph[node]:
            if ne not in visited:
                self.dfs(ne,visited,graph,top)
                
            elif self.recStack[ne]:
                self.cycle = True
                
        self.recStack[node] = False        
        top.append(node)
        
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        self.cycle = False
        for edge in prerequisites:
            
            graph[edge[1]].append(edge[0])
            
        visited = set()
        stk = []
        top = []
        self.recStack = defaultdict(bool)
        for i in range(numCourses):
            
            if i not in visited:
                self.dfs(i,visited,graph,top)
                
                
        answer = top[::-1]
        
        if self.cycle==True:
            return []
        

        
        return answer