class Solution:
    def twoEggDrop(self, n: int) -> int:
        
        k = 2
        matrix = [[float('inf') for i in range(0,n+1)] for j in range(0,3)]
        print(matrix)
        
        for i in range(0,3):
            matrix[i][0] = 0
            matrix[i][1] = 1
            
        for j in range(0,n+1):
            matrix[0][j] = 0
            matrix[1][j] = j
            
        for i in range(2,n+1):
            for j in range(2,k+1):
                matrix[j][i] = float('inf')
                for x in range(1, i + 1):
                    temp = 1+max(matrix[j-1][x-1],matrix[j][i-x])
                    matrix[j][i] = min(temp,matrix[j][i])
                    
        return matrix[2][n]