class Solution:
    
    def dfs(self,node,graph,ne,val):
        if node not in graph:
            return 0
        
        ans = -float('inf')
        for itr in graph[node]:
            ans = max(ans,self.dfs(itr,graph,node,val)+graph[node][itr])
            
        return ans 
    
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if len(manager) == 1:
            return 0
        
        graph = defaultdict(dict)
        
        for node in range(n):
            graph[manager[node]][node] = informTime[node]
        # print(graph)    
        root = list(graph[-1].keys())[0]
        rootWt = graph[-1][root]
        
        visited = set()
        val = 0
        return self.dfs(root,graph,root,rootWt)+rootWt