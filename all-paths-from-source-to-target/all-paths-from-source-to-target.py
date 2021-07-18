class Solution:
    ans = []
    def backtrack(self,node,path,target,graph):
        if node == target:
            self.ans.append(list(path))
            return
        
        for i in graph[node]:
            path.append(i)
            self.backtrack(i,path,target,graph)
            path.pop()
    
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.ans=[]
        path = deque([0])
        target = len(graph) -1
        self.backtrack(0,path,target,graph)
        return (self.ans)