class Solution:
    def dfsutil_cycletest(self,node,visited,stack,graph):
        visited.append(node)
        stack.append(node)
        
        for n in graph[node]:
            if n not in visited:
                if(self.dfsutil_cycletest(n,visited,stack,graph)):
                    return True
            
                
            elif n in stack:
                    return True
                
        stack.pop()
        return False
            
                
            
    
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        visited = []
        stack = []
        graph = {i:[] for i in range(1,n+1)}
    
        
        for i in relations:
            graph[i[0]].append(i[1])
            
        print(graph)
        
        cycle_test = False
        
        for i in range(1,n+1):
            if i not in visited:
                if(self.dfsutil_cycletest(i,visited,stack,graph)):
                    cycle_test = True
                    break
                    
        if cycle_test:
            return -1
        
        visited_length = {}
        def dfs_max_path(node: int) -> int:
            # return the longest path (inclusive)
            if node in visited_length:
                return visited_length[node]
            max_length = 1
            for end_node in graph[node]:
                length = dfs_max_path(end_node)
                max_length = max(length+1, max_length)
            # store it
            visited_length[node] = max_length
            return max_length

        return max(dfs_max_path(node)for node in graph.keys())
        
        
                