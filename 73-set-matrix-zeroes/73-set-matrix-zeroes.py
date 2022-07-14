class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        dq = deque()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                
                if matrix[i][j]==0:
                    dq.append((i,j))
                    
        while dq:
            
            x,y = dq.popleft()
            
            for i in range(len(matrix)):
                matrix[i][y] = 0
                
            for j in range(len(matrix[0])):
                matrix[x][j] = 0
                
        return matrix
                