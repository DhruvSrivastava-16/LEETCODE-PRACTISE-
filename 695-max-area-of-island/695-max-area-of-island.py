from collections import deque

class Solution:
    def isValid(self, grid, row, col, visited):
        
        if row<0 or col<0 or len(grid[0])<=col or len(grid)<=row:
            return False
        
        if (row, col) in visited:
            return False
        
        return True
    
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dx = [0,1,0,-1]
        dy = [-1,0,1,0]
        
        dq = deque()
        visited = set()
        Counts = set()
        count = 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if (i,j) not in visited and grid[i][j]==1:
                    visited.add((i,j))
                    dq.append([i,j])
                    count = 1
                    
                    while dq:
                        
                        elx, ely = dq.popleft()
                        
                        for itr in range(4):
                            tx = elx + dx[itr]
                            ty = ely + dy[itr]
                            
                            if self.isValid(grid,tx,ty,visited) and grid[tx][ty]==1:
                                
                                count+=1
                                visited.add((tx,ty))
                                dq.append([tx,ty])
                                
                    Counts.add(count)

        if Counts:
            print(Counts)
            return max(Counts)
        
        return 0
                    
                    
            
        
        