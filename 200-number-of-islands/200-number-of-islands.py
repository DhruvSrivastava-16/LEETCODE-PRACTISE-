from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        dq = deque()
        
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == "1":
                    dq.append((i,j))
                    grid[i][j] = "0"
                    count+=1
                    
                    
                    
                    while dq:
                        
                        x,y = dq.popleft()
                        
                        for itr in range(4):
                            
                            tx = x + dx[itr]
                            ty = y + dy[itr]
                            
                            if tx>=0 and ty>=0 and tx<len(grid) and ty<len(grid[0]) and grid[tx][ty] == "1":
                                dq.append((tx,ty))
                                grid[tx][ty] = "0"
                                
        return count
                            # ty = 
                        
                        
                    
                                
                    
                    
                
            
            
            