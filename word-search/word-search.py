class Solution:
    def check(self,i,j,board,word):
        if len(word)==0:
            return True
        
        if i<0 or j<0 or i>=len(board) or j>=len(board[0]):
            return False
        
        if board[i][j]!=word[0]:
            return False
        
        board[i][j] = '#'
        
        for d in [(-1,0),(1,0),(0,1),(0,-1)]:
            di = i + d[0]
            dj = j + d[1]
            if self.check(di,dj,board,word[1:]):
                return True
            
        board[i][j] = word[0]
            
        return False
            
        
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if self.check(i,j,board,word):
                    return True
                
                
        return False
        
        
        
        
        