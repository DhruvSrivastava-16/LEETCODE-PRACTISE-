class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        r_done = set()
        col_done = set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    r_done.add(i)
                    col_done.add(j)
                    
        print(r_done,col_done)
        
        for i in r_done:
            for j in range(0,len(matrix[0])):
                matrix[i][j] = 0
                
        for i in col_done:
            for j in range(0,len(matrix)):
                matrix[j][i] = 0
                
        return(matrix)
                
                