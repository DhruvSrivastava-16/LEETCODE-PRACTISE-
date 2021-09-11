class Solution:
    def dfs(self,start,graph,end):
        
        print(start)
        self.visited.add(start)
        if start == end:
            return True
        
        for n in graph[start]:
            if n not in self.visited:
                if self.dfs(n,graph,end):
                    return True        
        
        
    
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        graph = [[] for i in range(n)]
        
        for j in edges:
                
            graph[j[0]].append(j[1])
            graph[j[1]].append(j[0])

        print(graph)
        
        self.visited = set()
        if self.dfs(start,graph,end):
            return True
        
        return False