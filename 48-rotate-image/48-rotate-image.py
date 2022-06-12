
class Solution:
    
    def transpose(self, matrix):
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        for i in range(rows):
            for j in range(i+1,cols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                # print(matrix[i][j], matrix[j][i])
        
        
        
        
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        self.transpose(matrix)
        for row in range(len(matrix)):
            matrix[row] = matrix[row][::-1]

            
        
        
