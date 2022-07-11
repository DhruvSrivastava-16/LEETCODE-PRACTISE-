class Solution:
    
    def bt(self,i,j,temp2,temp,board,visited):
        
        if len(temp)==0:
            return True
        
        if i<0 or j<0 or i>=len(board) or j>=len(board[0]):
            return False
        
        if (i,j) in visited:
            return False
        
        if temp[0]!=board[i][j]:
            return False
        
        visited.add((i,j))
        
        left = self.bt(i,j-1,temp[1:],temp[1:],board,visited)
        right = self.bt(i,j+1,temp[1:],temp[1:],board,visited)
        down = self.bt(i-1,j,temp[1:],temp[1:],board,visited)
        up = self.bt(i+1,j,temp[1:],temp[1:],board,visited)
        
        visited.remove((i,j))
        
        return left or right or down or up
        
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        temp = []
        visited = set()
        
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                temp = ''
                visited = set()
                rq = self.bt(i,j,temp,word,board,visited)
                
                if rq:
                    return True
                
        return False
        
        
        