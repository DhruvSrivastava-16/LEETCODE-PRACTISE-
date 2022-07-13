class Solution:
    
    def dfs(self,nmr,dnr,graph,answer,temp,visited):
    
        
        if nmr==dnr and nmr not in visited:
            visited.add(nmr)
            answer.append(temp)
            return 
        
        if nmr in visited:
            return 
        
        visited.add(nmr)
        
        for keys in graph[nmr]:
            if keys not in visited:
                temp = temp*graph[nmr][keys]
                self.dfs(keys,dnr,graph,answer,temp,visited)
                temp = temp/graph[nmr][keys]
        
        visited.remove(nmr)
        
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        var  = set()
        graph = defaultdict(dict)
        for itr in range(len(equations)):
            graph[equations[itr][0]][equations[itr][1]]=values[itr]
          
            graph[equations[itr][1]][equations[itr][0]]=1/values[itr]
            var.add(equations[itr][0])
            var.add(equations[itr][1])
            
        answer = []
        
        for qr in queries:
            temp = 1
            visited = set()
            if qr[0] not in var or qr[1] not in var:
                answer.append(-1)
                continue
                
            if qr[0]==qr[1]:
                answer.append(1)
                continue
                
            prev = len(answer)
            
            self.dfs(qr[0],qr[1],graph,answer,temp,visited)
            
            if prev==len(answer):
                answer.append(-1)
            
        return answer
            
