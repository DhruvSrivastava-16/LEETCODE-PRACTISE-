class TicTacToe:

    def __init__(self, n: int):
        self.rows = {1:[0 for i in range(n)],2:[0 for i in range(n)]}
        self.columns = {1:[0 for i in range(n)],2:[0 for i in range(n)]}
        self.leftDiag = {1:0,2:0}
        self.rightDiag = {1:0,2:0}
        self.seen = set()
        self.sz = n
        

    def move(self, row: int, col: int, player: int) -> int:
        
        if (row,col) not in self.seen:
            self.seen.add((row,col))
            
        else:
            return
        
        # if self.rows
            
        self.rows[player][row]+=1
        if self.rows[player][row]==self.sz:
            return player
        
        self.columns[player][col]+=1
        if self.columns[player][col]==self.sz:
            return player

        
        if row-col==0:
            self.leftDiag[player]+=1
            
            if self.leftDiag[player]==self.sz:
                print(self.leftDiag)
                return player
            
        if row+col==self.sz-1:
            self.rightDiag[player]+=1
            
            if self.rightDiag[player]==self.sz:
                print(self.rightDiag)
                return player
        
        
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)