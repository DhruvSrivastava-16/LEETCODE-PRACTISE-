class Solution:
    def DFS(self,node,Visited,edges):
        adj = [i[1] for i in edges if i[0] == node]
        Visited.append(node)
        for i in adj:
            if i not in Visited:
                self.DFS(i,Visited,edges)
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        Visited = []
        cc = 0
        
        edges2 = [[i[1],i[0]] for i in edges]
        edges = edges + edges2
        for i in range(0,n):
            if i not in Visited:
                self.DFS(i,Visited,edges)
                cc+=1
                
        print(Visited)
        return cc;
                
        