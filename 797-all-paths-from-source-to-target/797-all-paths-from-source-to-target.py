class Solution:
    
    def backtrack(self, graph, path, paths, ne):
        path.append(ne)

        if ne == len(graph)-1:
            paths.append(path[:])
            return
            
        for neg in graph[ne]:
            self.backtrack(graph,path,paths,neg)
            path.pop()
            
    
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        path = [0]
        
        for ne in graph[0]:
            self.backtrack(graph,path,paths,ne)
            path = [0]
        
        return(paths)