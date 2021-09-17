import collections

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
        
            
    
    def DFS(self,node,stk,vis):
        
        vis.add(node)
        for n in self.graph[node]:
            if n not in vis:
                self.DFS(n,stk,vis)
                
        stk.append(node)
            
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.graph = [[] for i in range(0,numCourses)]
        
        for i in prerequisites:
            self.graph[i[0]].append(i[1])
            
        
        stk = []
        vis = set()
        
        for i in range(numCourses):
            if i not in vis:
                self.DFS(i,stk,vis)
                
        stk_ans = stk[:]
        visited = {}
        self.recstk = {i:False for i in range(0,numCourses)}

        for cc in stk_ans:

            if cc in visited:
                continue 

            stk = []

            if self.isCyclic(visited,cc,stk):
                return []
            
        return stk_ans
            