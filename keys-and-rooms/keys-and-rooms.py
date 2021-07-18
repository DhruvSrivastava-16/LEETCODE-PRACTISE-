class Solution:
    def DFSUtil(self,rooms,node,visited):
        visited.append(node)
        
        for i in rooms[node]:
            if i not in visited:
                self.DFSUtil(rooms,i,visited)
                
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = []
        self.DFSUtil(rooms,0,visited)
        print(visited)
        
        for i in range(0,len(rooms)):
            if i not in visited:
                return False
            
        return True