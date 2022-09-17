  
                            
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        queue = deque([])
        M, N = len(board), len(board[0])
        queue.append(click)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        corner = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
        while queue:
            r, c = queue.popleft()
			# should only visit the cell if it is M or E, after visited the cell should be 'B', 'M' or '1' - '8'
			# so we don't need visited matrix for recording.
            if board[r][c] == 'M':
                board[r][c] = 'X'
            elif board[r][c] == 'E':
                num_mines = 0
                for y,x in corner + directions:
                    dr = r + y
                    dc = c + x
                    if 0 <= dr < M and 0 <= dc < N and board[dr][dc] == 'M':
                        num_mines += 1
                board[r][c] = str(num_mines) if num_mines > 0 else 'B'
				# only relax node if the current visited cell is 'B'
                if num_mines == 0:
                    for y,x in corner + directions:
                        dr = r + y
                        dc = c + x
                        if 0 <= dr < M and 0 <= dc < N and (board[dr][dc] == 'E' or board[dr][dc] == 'M'):
                            queue.append([dr, dc])         
        return board
                    
                
            
            