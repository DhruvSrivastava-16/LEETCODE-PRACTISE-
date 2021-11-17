dx = [-1,0,1,0]
dy = [0,1,0,-1]

from collections import deque

class Solution:
    
    def isValid(self,grid,x,y,visited):
        if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]):
            return False
        
        if (x,y) in visited:
            return False
        
        if grid[x][y] == -1:
            return False
        
        return True
    
    
    
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        visited = set()
        dq = deque()
        
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    dq.append((i,j))
                    
            
        while dq:
            
            temp = dq.popleft()
            visited.add((temp[0],temp[1]))
            for i in range(4):
                tx = temp[0] + dx[i]
                ty = temp[1] + dy[i]
                
                if self.isValid(rooms,tx,ty,visited):
                    visited.add((tx,ty))
                    dq.append((tx,ty))

                    if rooms[tx][ty] > rooms[temp[0]][temp[1]]+1:
                        rooms[tx][ty] = rooms[temp[0]][temp[1]]+1
                        
                        
       
            