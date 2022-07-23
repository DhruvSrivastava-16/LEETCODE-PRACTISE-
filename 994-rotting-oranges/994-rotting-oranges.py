from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        
        dq = deque()
        countFresh = 0
        visited = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == 2:
                    dq.append([[i,j],0])
                    visited.add((i,j))
                    
                if grid[i][j] == 1:
                    countFresh += 1
           
        if not dq:
            
            if countFresh==0:
                return 0
            
            return -1
        
    
                    
        while dq:
        
            
            loc, time = dq.popleft()
            

            
            x = loc[0]
            y = loc[1]
                
            
            for i in range(4):
            
                tx = x + dx[i]
                ty = y + dy[i]
                
                if tx>=0 and ty>=0 and tx<len(grid) and ty<len(grid[0]) and (tx,ty) not in visited and grid[tx][ty]==1:
                    
                    

                    grid[tx][ty] = 2
                    visited.add((tx,ty))
                    dq.append([[tx,ty],time+1])
                    countFresh-=1
                    
        if countFresh == 0:
            print(grid)
            return time
                    
        print(grid)        
        return -1