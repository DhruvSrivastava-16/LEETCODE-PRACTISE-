class Solution:
    
    def dfs(self,board,visited,dq,point):
        i = point[0]
        j = point[1]
        
        if i<0 or j<0 or i>=len(board) or j>=len(board[0]):
            return False
        
        if board[i][j] == "X":
            return True
        
        if (i,j) in visited:
            return True
        
        visited.add(point)
        dq.append(point)
        
        up = self.dfs(board,visited,dq,(i-1,j))
        down = self.dfs(board,visited,dq,(i+1,j))
        left = self.dfs(board,visited,dq,(i,j-1))
        right = self.dfs(board,visited,dq,(i,j+1))
        
        return up and down and left and right
        
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        visited = set()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if (i,j) not in visited and board[i][j] == "O":
                    
                    dq = deque()
                    validity = self.dfs(board,visited,dq,(i,j))
                    if validity:
                        for x,y in dq:

                            board[x][y] = "X"
                    
                    
                
                
                