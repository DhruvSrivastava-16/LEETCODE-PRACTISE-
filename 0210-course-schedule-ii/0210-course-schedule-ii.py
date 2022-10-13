class Solution:

#     def dfs(self,node,graph,visited,recStack,top):
        
#         visited.add(node)
#         recStack[node] = True
        
#         for ne in graph[node]:
#             if ne not in visited:
#                 self.dfs(ne,graph,visited,recStack,top)
                
#             elif recStack[ne] == True:
#                 print("Cycle!")
#                 return 
            
#         recStack[node] = False
#         top.append(node)
                
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        indegree = {i:0 for i in range(numCourses)}
        dq = deque()
        top = []
        
        for preq in prerequisites:
            
            graph[preq[1]].append(preq[0])
            indegree[preq[0]]+=1
            
        for key in indegree.keys():
            if indegree[key] == 0:
                dq.append(key)
            
        while dq:
            node = dq.popleft()
            top.append(node)
            
            for ne in graph[node]:
                indegree[ne]-=1
                if indegree[ne] == 0:
                    dq.append(ne)
        
        if len(top) != numCourses:
            return []
        
        return top
            