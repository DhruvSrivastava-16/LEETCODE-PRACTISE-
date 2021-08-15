class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ans = [[0 for i in range(0,len(matrix[0]))]for j in range(0,len(matrix))]
        
        for i in range(0,len(matrix[0])):
            ans[0][i] = matrix[0][i]
        
        for j in range(0,len(matrix)):
            ans[j][0] = matrix[j][0]
            
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == 1:
                    ans[i][j] = min(ans[i-1][j],ans[i-1][j-1],ans[i][j-1])+1
                else:
                    ans[i][j] = 0
                    
        print(ans)
        sum1=0
        for j in ans:
            sum1 = sum1+sum(j)
        return(sum1)
       