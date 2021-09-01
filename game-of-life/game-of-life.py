class Solution:
    
    def isValid(self,board,i,j):
        
        if i>=len(board) or j>=len(board[0]) or i<0 or j<0:
            return False
        
        return True
        
    
    def sim(self,board,i,j):
        live_n = 0
        dead_n = 0
        
        for n in self.neighbours:
            
            tx = i+n[0]
            ty = j+n[1]
            
            if self.isValid(board,tx,ty):
                
                if board[tx][ty] == 1:
                    live_n +=1
                
                else:
                    dead_n +=1
        
        if live_n<2:
            #print('Less than 2')
            self.answer[i][j] = 0
            
        elif live_n>3:
            #print('More than 3')
            self.answer[i][j] = 0
            
        if board[i][j]==0 and live_n == 3:
            #print("Alive!")
            self.answer[i][j] = 1
                    

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        self.answer = [[board[i][j] for j in range(0,len(board[0]))] for i in range(0,len(board))]
        
        self.neighbours = [[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0]]
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                self.sim(board,i,j)
                
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                
                board[i][j] = self.answer[i][j]
                
        
                
