class Solution:
    
    def isValid(self,x,y,grid,visited):
        
        if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]):
            return False
        
        if (x,y) in visited:
            return False
        
        
        if grid[x][y] == '0':
            return False
        
        return True
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        dq = deque()
        count = 0
        
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                
                if grid[i][j] == '1' and (i,j) not in visited:
                    count+=1
                    dq.append([i,j])
                    visited.add((i,j))
                    
                
                # else:
                    # continue 
                    
                while dq:
                    
                    x,y = dq.popleft()
                    
                    for itr in range(4):
                        
                        tx = x+dx[itr]
                        ty = y+dy[itr]
                        
                        if self.isValid(tx,ty,grid,visited):
                            
                            dq.append([tx,ty])
                            visited.add((tx,ty))
                            
        return count
                        