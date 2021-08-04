from collections import deque
dirx = [-1,0,1,0]
diry = [0,1,0,-1]

class Solution:
    
    def isValid(self,x,y,grid):
        M = len(grid)
        N = len(grid[0])
        
        
        if x<0 or y<0 or x>=M or y>=N:
            return False
        
        if grid[x][y] == '0':
            return False
        
        #print("grid[x][y]",grid[x][y])
        return True
    
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 
        
        q = deque()
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == '1':
                    count+=1
                    grid[i][j] = 0
                    #print('-> ',i,j)
                    q.append((i,j))
                    
                    while len(q)>0:
                        #print('-----',q)
                        temp = q.popleft()
                        
                        for k in range(0,4):
                            tempx = temp[0]+dirx[k]
                            tempy = temp[1]+diry[k]
                            #print(tempx,tempy)
                            
                            if(self.isValid(tempx,tempy,grid)):
                                #print("in:")
                                q.append((tempx,tempy))
                                grid[tempx][tempy] = '0'
        
        print("Grid",grid)
        return count
                        