class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        for i in range(0,len(matrix)):
            for j in range(i+1,len(matrix[0])):
                
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] 
                
        for row in range(len(matrix)):
            matrix[row] = matrix[row][::-1]
            