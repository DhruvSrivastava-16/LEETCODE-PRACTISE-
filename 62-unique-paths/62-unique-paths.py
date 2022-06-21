class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
    
        d = [[1 for i in range(n)] for j in range(m)]
        for col in range(1,n):
            for row in range(1,m):
                
                d[row][col] = d[row-1][col] + d[row][col-1]
        
        print(d)
        return d[-1][n-1]
        
        