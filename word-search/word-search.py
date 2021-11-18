class Solution:
    
    def backtrack(self,board,word,i,j):
        if len(word)==0:
            return True
        
        if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j]!=word[0]:
            return False
        
        board[i][j] = '#'
        
        for k in [(-1,0),(0,1),(1,0),(0,-1)]:
            
            if self.backtrack(board,word[1:],i+k[0],j+k[1]):
                return True
            
        board[i][j] = word[0]
        
        return False
            
            
        
        
        
    
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.backtrack(board,word,i,j):
                    return True
                
        return False