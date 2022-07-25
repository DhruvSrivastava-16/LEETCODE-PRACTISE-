class Solution:
    def defaultRec(self):
        return False

    
    def isCyclicUtil(self, v, graph,visited, parent):
 
        # Mark the current node as visited
        visited.add(v) 
 
        # Recur for all the vertices
        # adjacent to this vertex
        for i in graph[v]:
 
            # If the node is not
            # visited then recurse on it
            if i not in visited:
                if(self.isCyclicUtil(i,graph ,visited, v)):
                    return True
            # If an adjacent vertex is
            # visited and not parent
            # of current vertex,
            # then there is a cycle
            elif parent != i:
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
        cycle = self.isCyclicUtil(0,graph,visited,None)
        print(cycle,visited)
        if cycle:
            return False
        
        if len(visited)==n:
            return True
        
        return False
        