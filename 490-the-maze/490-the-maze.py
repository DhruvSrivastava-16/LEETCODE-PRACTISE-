class Solution:
    
    di = [(-1,0),(0,1),(1,0),(0,-1)]
    
    def dfs(self,maze,start,destination,visited):
        
        if start[0]<0 or start[1]<0 or start[1]>=len(maze[0]) or start[0]>=len(maze):
            return False
        
        if start == destination:
            return True
        
        if (start[0],start[1]) in visited:
            return False
        
        visited.add((start[0],start[1]))
        
        tx = start[0]
        ty = start[1]
        
        left = ty-1
        right = ty+1
        down = tx+1
        up = tx-1

        while tx>=0 and left>=0 and tx<len(maze) and maze[tx][left]!=1:
            left-=1
                
        if self.dfs(maze,[tx,left+1],destination,visited):
            return True
        
        while tx>=0 and right>=0 and tx<len(maze) and right<len(maze[0]) and maze[tx][right]!=1:
            right+=1
                
        if self.dfs(maze,[tx,right-1],destination,visited):
            return True
        
        while up>=0 and ty>=0 and up<len(maze) and ty<len(maze[0]) and maze[up][ty]!=1:
            up-=1
                
        if self.dfs(maze,[up+1,ty],destination,visited):
            return True

        while down>=0 and ty>=0 and down<len(maze) and ty<len(maze[0]) and maze[down][ty]!=1:
            down+=1
                
        if self.dfs(maze,[down-1,ty],destination,visited):
            return True

                
            
        return False
                
            

    
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        self.di = [(-1,0),(0,1),(1,0),(0,-1)]
        visited = set()
        answer = self.dfs(maze,start,destination,visited)
        print('A:',answer)
        return (answer)
        