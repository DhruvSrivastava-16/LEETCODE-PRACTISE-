class Solution:
    
    def __init__(self):
        self.m = 0
        self.n = 0
        self.candyToCrush = set()
    
    def getCandiesToCrush(self, x, y, board):
        """ Get indices of the candies that needs to be crushed """
        # for non-zero values
        
        val = board[x][y]
        
        if val!=0:
             
            if x+2<self.m and board[x+1][y]==board[x+2][y] and board[x+2][y]==val:
                self.candyToCrush.add((x,y))
                self.candyToCrush.add((x+1,y))
                self.candyToCrush.add((x+2,y))

            if y+2<self.n and board[x][y+1]==board[x][y+2] and board[x][y+2]==val:
                self.candyToCrush.add((x,y))
                self.candyToCrush.add((x,y+1))
                self.candyToCrush.add((x,y+2))

            
    def crushCandies(self, board):
        """ Crush the candies by replacing the candy id to 0 """
        
        for vals in self.candyToCrush:
            board[vals[0]][vals[1]] = 0
            
        return board

    def applyGravity(self, board):
        """ Drop the candies """
        for j in range(self.n):
            # initialize top, bottom
            top = bottom = self.m - 1
            while top >= 0:
                if board[top][j] != 0:
                    board[bottom][j], board[top][j] = board[top][j], board[bottom][j]
                    bottom-=1
                top-=1
        # return board
    
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        self.m = len(board)
        self.n = len(board[0])
        
        # reset the hashset
        self.candyToCrush = set()

        for i in range(self.m):
            for j in range(self.n):
                self.getCandiesToCrush(i, j, board)
		
		# stable state achieved
        if len(self.candyToCrush) == 0:
            return board

        # crush candies
        self.crushCandies(board)

        # apply gravity
        self.applyGravity(board)
            
        return self.candyCrush(board)