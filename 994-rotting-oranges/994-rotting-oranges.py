from collections import deque
class Solution:
    
    def valid(self,grid,txx,tyy):
        if txx<0 or txx>=len(grid) or tyy<0 or tyy>=len(grid[0]):
            return False
        
        return True


    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        dq = deque()
        mins = -1
        ones = 0
        startLoc = None
        dq = deque()

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j]==2:
                    dq.append([i,j])
                
                elif grid[i][j]==1:
                    ones+=1
        
        if not dq:
            
            if ones>0:
                return -1
            
            else:
                return 0
        
        if ones==0:
            return 0
                    
        visited = set()
        dq.append([-1,-1])

        
        while dq:
            tx, ty = dq.popleft()
            visited.add((tx,ty))
            
            if tx == -1:
                
                mins+=1
                
                if dq:
                    dq.append([-1,-1])
                continue

            for itr in range(4):

                txx = tx + dx[itr]
                tyy = ty + dy[itr]

                if self.valid(grid,txx,tyy) and grid[txx][tyy]==1 and (txx,tyy) not in visited:
                    grid[txx][tyy]=2
                    dq.append([txx,tyy])
                    visited.add((txx,tyy))
                    ones-=1

                
                        
        print(grid,mins,ones)
        if ones>0:
            return -1
        
        return mins
                        
                        
                        
                    
                    
                    