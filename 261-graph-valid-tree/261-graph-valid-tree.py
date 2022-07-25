class Solution:
    def defaultRec(self):
        return False

    
    def DFS(self,node,graph,recStk,visited,Parent):
        visited.add(node)
        
        for n in graph[node]:
            if n not in visited:
                if self.DFS(n,graph,recStk,visited,node):
                    return True
            
            elif Parent!=n:
                print(Parent,n,node)
                return True
            
        return False
        
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        recStk = defaultdict(self.defaultRec)
        
        visited = set()
        cycle = False
        cycle = self.DFS(0,graph,recStk,visited,None)
        print(cycle,visited)
        if cycle:
            return False
        
        if len(visited)==n:
            return True
        
        return False
        