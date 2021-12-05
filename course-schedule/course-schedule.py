class Solution:
    def isCyclic(self,visited,cc,stk):
        visited[cc] = True
        self.recstk[cc] = True
        
        for n in self.graph[cc]:
            
            if n not in visited:
                if self.isCyclic(visited,n,stk):
                    return True
            
            elif self.recstk[n] == True:
                return True
        
        self.recstk[cc] = False
        return False
        
        
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        self.graph = {i:[] for i in range(0,numCourses)}
        self.recstk = {i:False for i in range(0,numCourses)}
        for i in prerequisites:
            
            self.graph[i[1]].append(i[0])
            
           
        
        visited = {}
        stk = []
                
        for cc in range(numCourses):
            
            if cc in visited:
                continue 
            
            stk = []
            
            if self.isCyclic(visited,cc,stk):
                return False
            
            
        return True
                
        print(self.graph)