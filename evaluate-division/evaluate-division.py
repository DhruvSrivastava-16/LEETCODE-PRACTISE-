from collections import defaultdict

class Solution:
    def doDFS(self,graph,visited,root,target,prod):
        print("STEP:",root,target)
        ret = -1
        if target in graph[root]:
            return prod*graph[root][target]
       
        neighbours = graph[root]
        visited.add(root)
        
        for n,v in neighbours.items():
            if n not in visited:
                print("Multi",n,graph[root][n] )
                ret = self.doDFS(graph,visited,n,target,prod*graph[root][n])
                if ret!=-1:
                    break
               
        return ret
        
        
    
    def calcEquation(self, eq: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        
        graph = defaultdict(dict)
        
        for i in range(len(eq)):
            graph[eq[i][0]][eq[i][1]] = values[i]
            
            graph[eq[i][1]][eq[i][0]]=1/values[i]
        
        print(graph)
        
        results = []
        for q in queries:
            print(q)
            if q[0] not in graph or q[1] not in graph:
                results.append(-1)
            
            elif q[0] == q[1]:
                # print('ye:',q)
                results.append(1) 
                
            else:
                visited = set()
                print("FOR",q)
                results.append(self.doDFS(graph,visited,q[0],q[1],1))
                
        return(results)
            
            
        
        