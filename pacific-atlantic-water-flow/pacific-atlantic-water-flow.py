dx = [-1,0,1,0]
dy = [0,1,0,-1]

class Solution:
    def isValid(self,x,y,nr,nc,reachable):
        if x<0 or y<0 or x>=nr or y>=nc:
            return False
        
        if (x,y) in reachable:
            return False
        
        return True
        
        
    def bfs(self,queue,num_rows, num_cols,heights):
        reachable = set()
        while queue:
            x,y = queue.popleft()
            reachable.add((x,y))
            
            for i in range(0,4):
                tx = x+dx[i]
                ty = y+dy[i]
                
                if self.isValid(tx,ty,num_rows, num_cols,reachable):
                    if heights[tx][ty]>=heights[x][y]:
                        queue.append((tx,ty))
                        
        return reachable
                        
                
                
                
            
            
            
            
    
    
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]: 
            return []
            
        num_rows, num_cols = len(matrix), len(matrix[0])
        pacific_queue = deque()
        atlantic_queue = deque()
        
        for i in range(num_rows):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, num_cols - 1))
            
        for i in range(num_cols):
            pacific_queue.append((0, i))
            atlantic_queue.append((num_rows - 1, i))
        
        
        
        pacific_reachable = self.bfs(pacific_queue,num_rows, num_cols,matrix)
        atlantic_reachable = self.bfs(atlantic_queue,num_rows, num_cols,matrix)
        
        return list(pacific_reachable.intersection(atlantic_reachable))