class Solution:
    
    def dfs(self,node,visited,graph,top):
        visited.add(node)
        self.recStack[node] = True
        for ne in graph[node]:
            if ne not in visited:
                if self.dfs(ne,visited,graph,top):
                    return True
                
            elif self.recStack[ne]:
                return True
                
        self.recStack[node] = False        
        top.append(node)
        return False
        
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        for edge in prerequisites:
            
            graph[edge[1]].append(edge[0])
            
        visited = set()
        stk = []
        top = []
        self.recStack = defaultdict(bool)
        for i in range(numCourses):
            
            if i not in visited:
                if self.dfs(i,visited,graph,top):
                    return []
                
                
        answer = top[::-1]
        

        

        
        return answer