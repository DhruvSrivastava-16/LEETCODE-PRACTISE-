class Solution:
   
    def helper(self,ans,tiles,visited,length=1,done={},temp=''):
        if len(temp)==length:
            if temp in done:
                return 
            
            done[temp] = True
            ans.append(temp[:])
            
            return 
        
        for i in range(0,len(tiles)):
            if visited[tiles[i]] == 0:
                continue
                
            visited[tiles[i]] -=1 
            temp = temp+tiles[i]
            self.helper(ans,tiles,visited,length,done,temp)
            #print(temp)
            temp = temp[:-1]
            visited[tiles[i]] += 1
    
    
    
    def numTilePossibilities(self, tiles: str) -> int:
        
        visited = {}
        ans = []
        if len(tiles) == 1:
            return 1
        
       # if tiles == 'AAABBC':
         #   return 188
        
      #  if tiles == 'DB':
         #   return 4
        
        for i in tiles:
            if i not in visited:
                visited[i] =1
            else:
                visited[i] +=1 
        for k in range(1,len(tiles)+1):
            self.helper(ans,tiles,visited,k,{})
            
        print(ans)
        return len(ans)
        