class Solution:
    def backtracking(self, board, temp, x,y,visited):

        
        if len(temp)==0:
            return True
        
        if x<0 or y<0 or x>=len(board) or y>=len(board[0]):
            return False
        
        if board[x][y]!=temp[0]:
            return False
        
        if (x,y) in visited:
            return False
        
        visited.add((x,y))
        
        one = self.backtracking(board,temp[1:],x+1,y,visited)
        two = self.backtracking(board,temp[1:],x,y+1,visited)
        three = self.backtracking(board,temp[1:],x-1,y,visited)
        four = self.backtracking(board,temp[1:],x,y-1,visited)
        
        visited.remove((x,y))
        
        
        return one or two or three or four
        
        
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        x, y = 0, 0
        temp = ''
        
        for x in range(0,len(board)):
            for y in range(0,len(board[0])):
                visited = set()
                ans = self.backtracking(board, word,x,y,visited)
                
                if ans:
                    return ans
                
        return False