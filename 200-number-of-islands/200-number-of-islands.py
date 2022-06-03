from collections import deque
dx = [1,0,-1,0]
dy = [0,1,0,-1]

class Solution:
    
    def isValid(self, row, col, mat, vis):
        
        if row<0 or col<0 or row>=len(mat) or col>=len(mat[0]):
            return False
        
        if vis[row][col] or mat[row][col]=='0':
            return False
        
        return True
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row = 0
        col = 0
        vis = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        
        dq = deque()
        
        num = 0
        
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                
                if grid[i][j] == '1' and not vis[i][j]:
                    dq.append([i,j])
                    num+=1
                    vis[i][j] = True
                    
        
                    while dq:

                        elx, ely = dq.popleft()

                        for itr in range(4):

                            eltx = elx + dx[itr]
                            elty = ely + dy[itr]

                            if self.isValid(eltx, elty, grid, vis):

                                dq.append([eltx, elty])
                                vis[eltx][elty] == True
                                grid[eltx][elty] = '0'
                    
                    
        return num
            
            
            
            
        
        
        
        