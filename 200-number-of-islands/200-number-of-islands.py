from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        
        dq = deque()
        count = 0
        visited = set()
        
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                
                if grid[i][j]=="1" and (i,j) not in visited:
                    dq.append((i,j))
                    count+=1
                    visited.add((i,j))
                    
                while dq:
                    
                    x,y = dq.popleft()
                    
                    for itr in range(4):
                        tx = dx[itr] + x
                        ty = dy[itr] + y
                        
                        if tx>=0 and tx<len(grid) and ty>=0 and ty<len(grid[0]):
                            
                            if grid[tx][ty] == "1" and (tx,ty) not in visited:
                                
                                dq.append((tx,ty))
                                visited.add((tx,ty))
                                
        return count
                                
                    
                    
                
            
            
            