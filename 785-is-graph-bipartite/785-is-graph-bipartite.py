from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        dq = deque()
        seen = set()
        colorMap = dict()
        
        for i in range(len(graph)):
            print(i)
            if i not in colorMap:
                
                dq.append((i,1))
                colorMap[i]=1
                
                while dq:
                    print(dq)
                    node, color = dq.popleft()
                    colorMap[node] = color
                    
                    for n in graph[node]:
                        print('ne:',n)
                        if n not in colorMap:
                            
                            dq.append((n,-color))
                            colorMap[n] = -color
                            
                        else:
                            if colorMap[n] == colorMap[node]:
                    
                                return False
                            
                            
        print(colorMap,dq)            
        return True
                    
                    
                    
                    