class Solution:
    
    def dfs(self,n,cMap,prev,graph,color):
    
        
        for node in graph[n]:
            if node not in cMap:
                cMap[node]=color
                if not self.dfs(node,cMap,n,graph,-color):
                    return False
                
            elif cMap[node]==cMap[n]:
                print(node,n)
                return False
            
        return True
    
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        cMap = {}
        graph = defaultdict(list)
        color = 1
        
        for i in dislikes:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
            
        for nd in range(1,n+1):
            if nd not in cMap:
                cMap[nd] = color
                if not self.dfs(nd,cMap,None,graph,-color):
                    print(cMap)
                    return False
        print(cMap)        
        return True