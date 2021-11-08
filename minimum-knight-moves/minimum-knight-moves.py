dirx = [-2,2,-2,2,1,-1,1,-1]
diry = [1,-1,-1,1,2,2,-2,-2]


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        
        visited = set()
        dq = deque()
        dq.append([0,0])
        visited.add((0,0))
        steps = 0
        
        while dq:
            
            for i in range(len(dq)):
                tx,ty = dq.popleft()
                if (tx,ty) == (x,y):
                    return steps

                for i in range(0,len(dirx)):
                    t_x = tx + dirx[i]
                    t_y = ty + diry[i]

                    if (t_x,t_y) not in visited:
                        visited.add((t_x,t_y))
                        dq.append([t_x,t_y])
                    
                    
            steps += 1
                
        return steps
        