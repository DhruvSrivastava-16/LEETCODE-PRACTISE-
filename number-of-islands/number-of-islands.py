dx = [-1,0,1,0]
dy = [0,1,0,-1]

class Solution:
    def isValid(self,x,y,grid):
        
        if x<0 or y<0 or y>=len(grid[0]) or x>=len(grid):
            return False
        
        if grid[x][y] == '0':
            return False
        
        return True
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        dq = deque()
        count = 0
        
        
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if (i,j) not in visited and grid[i][j]=='1':
                    dq.append((i,j))
                    grid[i][j]=='0'
                    count+=1
                    
                    
                while dq:
                    
                    temp = dq.popleft()
                    for x in range(4):
                        tx = temp[0]+dx[x]
                        ty = temp[1]+dy[x]
                        
                        if self.isValid(tx,ty,grid):
                            dq.append((tx,ty))
                            grid[tx][ty]='0'
                            
                            
        return count
                    
        
        