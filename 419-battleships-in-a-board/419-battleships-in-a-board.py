class Solution:
    
    counter = 0
    
    def dfs(self,board,x,y):
        # print('Curr:',board)
        xsz = 1
        ysz = 1
        answer = 0
        
        for xx in range(x,len(board)):
            if board[xx][y] == 'X':
                # print('X True',board,xx,y)
                board[xx][y] = '.'
            else:
                break
        board[x][y] = 'X'
        for yy in range(y,len(board[0])):
            
            if board[x][yy] == 'X':
                # print(board)
                # print('Y True',board,x,yy)

                board[x][yy] = '.'
            else:
                break
        answer = xsz+ysz-1
        
        return answer
            
    def countBattleships(self, board: List[List[str]]) -> int:
        self.counter = 0
        for x in range(len(board)):
            for y in range(len(board[0])):
                
                if board[x][y] == 'X':
                    
                    self.counter+=self.dfs(board,x,y)
                    # board[x][y] = '.'
                    
                    
        return self.counter