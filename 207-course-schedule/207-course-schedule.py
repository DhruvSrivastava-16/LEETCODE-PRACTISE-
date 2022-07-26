class Solution:
    
    def Top(self,graph,visited,recStack,stk,node):
        
        visited.add(node)
        recStack[node] = 1
        
        for n in graph[node]:
            if n not in visited:
                if self.Top(graph,visited,recStack,stk,n):
                    return True
                
            elif recStack[n]==1:
                return True
            
        stk.append(node)
        recStack[node]=0
        return False
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for preReq in prerequisites:
            
            graph[preReq[1]].append(preReq[0])
            
        stk = []
        visited = set()
        recStack = defaultdict(int)
        
        for i in range(0,numCourses):
            if i not in visited:
                if self.Top(graph,visited,recStack,stk,i):
                    return False
            
            
        return True