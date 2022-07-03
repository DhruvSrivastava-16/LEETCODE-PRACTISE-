from collections import deque
class Solution:
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        locs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        dq = deque()
        dq.append((0,0))
                
        if grid[0][0] == 1:
            return -1
        
        if grid[-1][-1]==1:
            return -1
        steps = []
        visited = set()
        visited.add((0,0))
        grid[0][0] = 1

        
        while dq:
            
            x, y = dq.popleft()
            dist = grid[x][y]
                
            steps.append([x,y])
            
            if x == len(grid)-1 and y == len(grid[0])-1:
                print(steps, dist)
                return dist
            
            
            
            for xx, yy in locs:
                
                tx = x + xx
                ty = y + yy
                
                if tx>=0 and tx<len(grid) and ty>=0 and ty<len(grid[0]):
                    
                    if grid[tx][ty]!=1 and (tx,ty) not in visited:
                        visited.add((tx,ty))
                        dq.append((tx,ty))
                        grid[tx][ty] = dist+1
                        
        return -1