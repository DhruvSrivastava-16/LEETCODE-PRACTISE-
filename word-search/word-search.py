class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if self.backtrack(i,j,word,board):
                    return True
                
        return False
    
    
    def backtrack(self,i,j,suffix,board):
        if len(suffix) == 0:
            return True

        if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j]!=suffix[0]:
            return False

        board[i][j] = '#'

        for rowOffset, colOffset in [(0, 1), (-1, 0), (0, -1), (1, 0)]:

            if self.backtrack(i+rowOffset,j+colOffset,suffix[1:],board):
                return True

        board[i][j] = suffix[0]

        return False