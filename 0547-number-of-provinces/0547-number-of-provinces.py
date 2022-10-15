class Solution:
    
    def dfs(self,cc,gph,visited,nd):
        
        visited.add(nd)
        for ne in range(len(gph[0])):
            if ne!=nd and ne not in visited and gph[nd][ne]==1:
                self.dfs(cc,gph,visited,ne)
                
                
    def findCircleNum(self, gph: List[List[int]]) -> int:
        
        
        
        nodes = len(gph)
        visited = set()
        cc = 0
        
        for nd in range(nodes):
            if nd not in visited:
                cc+=1
                self.dfs(cc,gph,visited,nd)
            
            
        return cc