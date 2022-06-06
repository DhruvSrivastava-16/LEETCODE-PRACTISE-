class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        columnWiseMax = []
        rowWiseMax = []
        
        for i in range(len(grid[0])):  
            temp = []
            for j in range(len(grid)):
                
                temp.append(grid[j][i])
                
            columnWiseMax.append(max(temp))

        for i in range(len(grid)):  
            temp = []
            for j in range(len(grid[0])):
                
                temp.append(grid[i][j])
                
            rowWiseMax.append(max(temp))
        
        ans = 0

        for i in range(len(grid)):  

            for j in range(len(grid[0])):
                
                ans+= min(rowWiseMax[i], columnWiseMax[j]) - grid[i][j]
        
        return ans
            
        