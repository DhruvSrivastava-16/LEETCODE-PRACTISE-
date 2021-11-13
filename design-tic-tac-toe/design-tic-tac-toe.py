from collections import defaultdict

class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0 for i in range(n)] for j in range(n)]
        
        
        self.h_map_idr = {i:[0,0] for i in range(n)}
        self.h_map_idc = {i:[0,0] for i in range(n)}   
        self.ld = [n,n]
        self.rd = [n,n]
        
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        self.h_map_idr[row][player-1]+=1
        self.h_map_idc[col][player-1]+=1
        
        if row == col:
            self.ld[player-1]-=1
            if self.ld[player-1]==0:
                return player
            
        if row+col == self.n-1:
            self.rd[player-1]-=1
            if self.rd[player-1]==0:
                return player
        
        
        if self.h_map_idr[row][player-1]==self.n:
            return player
        
        elif self.h_map_idc[col][player-1]==self.n:
            return player
        
        
        
        else:

            return 0
        
        
    