class Solution:
    
    def dfs(self,r,c,matrix,cache):
        dist = 0
        
        if cache[r][c]!=-float('inf'):
            return cache[r][c]
        
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        for i in range(len(dirs)):
            
            tx = r + dirs[i][0]
            ty = c + dirs[i][1]
            
            if tx<0 or ty<0 or tx>=len(matrix) or ty>=len(matrix[0]):
                continue
                
            if matrix[tx][ty]>matrix[r][c]:
                dist = max(cache[r][c],self.dfs(tx,ty,matrix,cache),dist)
        
        cache[r][c] = 1+dist
        
        return 1+dist
                
        
            
        
            
        
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        answer = -1
        cache = [[-float('inf') for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                
                temp = self.dfs(i,j,matrix,cache)
                answer = max(temp,answer)
                
        return answer