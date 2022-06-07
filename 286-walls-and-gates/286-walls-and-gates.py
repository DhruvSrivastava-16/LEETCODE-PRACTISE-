from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]
class Solution:
    def isValid(self,x,y,rooms,visited):
        if x<0 or y<0 or x>=len(rooms) or y>=len(rooms[0]):
            return False
        
        if (x,y) in visited:
            return False
        
        if rooms[x][y]==-1:
            return False
        
        return True
    
    
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        visited = set()
        dq = deque()
        for i in range(0,len(rooms)):
            for j in range(0,len(rooms[0])):
                
                if rooms[i][j] == 0:
                    
                    dq.append([i,j])
                    
        while dq:
            
            tx, ty = dq.popleft()
            visited.add((tx,ty))

            for itr in range(4):
                
                txx = tx + dx[itr]
                tyy = ty + dy[itr]
                
                if self.isValid(txx,tyy,rooms,visited):
                    
                    if rooms[txx][tyy]>rooms[tx][ty]+1:
                        rooms[txx][tyy] = rooms[tx][ty]+1
                        dq.append([txx,tyy])

                        
                    
                    
        