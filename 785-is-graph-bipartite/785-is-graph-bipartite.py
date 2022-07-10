from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        dq = deque()
        seen = set()
        colorMap = dict()
        
        for i in range(len(graph)):
            if i not in colorMap:
                
                dq.append((i,1))
                colorMap[i]=1
                
                while dq:
                    node, color = dq.popleft()
                    colorMap[node] = color
                    
                    for n in graph[node]:
                        if n not in colorMap:
                            
                            dq.append((n,-color))
                            colorMap[n] = -color
                            
                        else:
                            if colorMap[n] == colorMap[node]:
                    
                                return False
                            
                            
        print(colorMap,dq)            
        return True
                    
                    
                    
                    