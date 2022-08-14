class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        x, y = len(matrix)-1,0
        val = target
        
        while x>=0 and y<len(matrix[0]):
            print(matrix[x][y])
            if val==matrix[x][y]:
                return True
            
            elif val<matrix[x][y]:
                x-=1
                
            else:
                y+=1
                
                
        return False