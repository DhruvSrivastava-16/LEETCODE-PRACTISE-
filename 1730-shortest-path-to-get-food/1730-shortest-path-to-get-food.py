from collections import deque

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        
        
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        visited = set()
        dq = deque()
        
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                
                if grid[i][j]=='*':
                    stp = 0
                    dq.append([[i,j],stp])
                    visited.add((i,j))
                    
                    while dq:
                        
                        loc, step = dq.popleft()
                        
                        x = loc[0]
                        y = loc[1]
                        
                        if grid[x][y]=="#":
                            return step
                        
                        for itr in range(4):
                            tx = x+dx[itr]
                            ty = y+dy[itr]
                            
                            if tx>=0 and ty>=0 and tx<len(grid) and ty<len(grid[0]) and (tx,ty) not in visited:
                                
                                if grid[tx][ty]!='X':
                                    
                                    visited.add((tx,ty))
                                    dq.append(([tx,ty],step+1))
                                    
                                    
        return -1
                                    
        