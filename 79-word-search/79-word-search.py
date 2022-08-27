class Solution:
    
    
    def find(self,visited,tempWord,i,j,board):
        
        if len(tempWord) == 0:
            return True
        
        if (i,j) in visited:
            return 
        
        if i<0 or i>=len(board):
            return False
        
        if j<0 or j>=len(board[0]):
            return False

        if board[i][j] != tempWord[0]:
            return False
        
        visited.add((i,j))
        
        left = self.find(visited,tempWord[1:],i,j-1,board)
        right = self.find(visited,tempWord[1:],i,j+1,board)
        top = self.find(visited,tempWord[1:],i+1,j,board)
        down = self.find(visited,tempWord[1:],i-1,j,board)
        
        visited.remove((i,j))
        
        return left or right or top or down
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        tempWord = word
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                if self.find(visited,tempWord,i,j,board):
                    return True
                
        return False