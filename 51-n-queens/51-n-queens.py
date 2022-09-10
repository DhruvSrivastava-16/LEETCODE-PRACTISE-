class Solution:
    
    
    def backtrack(self,row,answer,temp,leftDiag,rightDiag,colSet):
        
        if row==len(temp):
            print(temp)
            tempanswer = []
            for row1 in temp:
                tempanswer.append(''.join(row1))
            answer.append(tempanswer[:])
            return 
        
        for i in range(len(temp[0])):
            
            c = i
            r = row
            
            if r-c not in leftDiag and r+c not in rightDiag and c not in colSet and temp[r][c]=='.':
                
                temp[r][c] = 'Q'
                leftDiag.add(r-c)
                rightDiag.add(r+c)
                colSet.add(c)
                
                
                self.backtrack(row+1,answer,temp,leftDiag,rightDiag,colSet)
                
                leftDiag.remove(r-c)
                rightDiag.remove(r+c)
                colSet.remove(c)
                temp[r][c] = '.'
        
        
    
    
    def solveNQueens(self, n: int) -> List[List[str]]:
    
        row = 0
        answer = []
        temp = []
        leftDiag = set()
        rightDiag = set()
        colSet = set()
        
        temp = [['.' for j in range(n)] for i in range(n)]
        
        self.backtrack(row,answer,temp,leftDiag,rightDiag,colSet)
        
        return answer