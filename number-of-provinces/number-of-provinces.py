
class Solution:
    
    def Util(self,node,visited,isConnected,sz):
        visited.append(node)
        
        for k in range(0,sz):
            if isConnected[node][k]==1 and k not in visited:
                self.Util(k,visited,isConnected,sz)
                
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        visited = []
        cc = 0
        sz = len(isConnected)
        for i in range(0,sz):
            
            if i not in visited:
                cc+=1
                self.Util(i,visited,isConnected,sz)
                
        return cc
                
            