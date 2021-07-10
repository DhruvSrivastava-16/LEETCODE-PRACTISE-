class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        triangle = []
        for rown_num in range(num_rows):
            temp_row = [None for _ in range(rown_num+1)]
            temp_row[0] = temp_row[-1] = 1
            
            for j in range(1,len(temp_row)-1):
                temp_row[j] = triangle[rown_num-1][j-1] + triangle[rown_num-1][j]
                
            triangle.append(temp_row)
            
        return triangle
                
        
        