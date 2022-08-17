class Solution:
    
    def dfs(self,visited,stack,node,graph,parent):
        visited.add(node)
        stack[node] = True
        for n in graph[node]:
            if n not in visited:
                if self.dfs(visited,stack,n,graph,node):
                    return True
                
            elif parent != n:
                return True
            
        stack[node] = False
        return False
    
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        visited = set()
        stack = {}
        
        cycle = self.dfs(visited,stack,0,graph,None)
        
        if len(visited)!=n:
            return False
        
        if cycle:
            return False
        
        return True
        
        