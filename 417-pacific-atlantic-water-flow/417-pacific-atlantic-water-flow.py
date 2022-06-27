from collections import deque
class Solution:
    
    def bfs(self,dq, heights):
        reach = set()
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        while dq:
            
            tx, ty = dq.popleft()
            reach.add((tx,ty))
            
            for itr in range(4):
                txx = tx + dx[itr]
                tyy = ty + dy[itr]
                
                if txx>=0 and txx<len(heights) and tyy>=0 and tyy<len(heights[0]) and (txx,tyy) not in reach:
                    
                    if heights[txx][tyy]>=heights[tx][ty]:
                        dq.append([txx,tyy])
                        
        return reach
                    
                    
                
                
            
            
            
    
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        pacific_queue = deque()
        atlantic_queue = deque()
        num_rows, num_cols = len(matrix), len(matrix[0])
        for i in range(num_rows):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, num_cols - 1))
        for i in range(num_cols):
            pacific_queue.append((0, i))
            atlantic_queue.append((num_rows - 1, i))
        
        pf = self.bfs(pacific_queue,matrix)
        # print(list(pf))
        al = self.bfs(atlantic_queue,matrix)
        # print(list(al))
        return(list(al.intersection(pf)))
        