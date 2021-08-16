class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        DIR = [-1,0,1,0,-1]
        nRow, nCol = len(grid), len(grid[0])
        
        for r in range(nRow):
            for c in range(nCol):
                if grid[r][c] == '*':
                    start = (r,c)
                    break
        
        visited = set()
        q = deque()
        q.append((start[0], start[1], 0))
        visited.add((start[0],start[1]))
        
        while q:
            r, c, level = q.popleft()
            
            if grid[r][c] == '#':
                return level
            
            for d in range(4):
                nr, nc = r + DIR[d], c + DIR[d+1]
                
                if nr < 0 or nc < 0 or nr >= nRow or nc >= nCol or grid[nr][nc] == "X" or ((nr,nc) in visited): continue
                
                q.append((nr, nc, level+1))
                visited.add((nr, nc))
        
        return -1