class Solution:
    
    def dfs(self,graph,node,visited):
        
        visited.add(node)
        
        for ne in graph[node]:
            if ne not in visited:
                self.dfs(graph,ne,visited)
                
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        
        for out in range(len(bombs)):
            for ins in range(len(bombs)):
                
                if out!=ins:
                    
                    fx,fy,fr = bombs[out]
                    sx,sy,sr = bombs[ins]
                    
                    if (fx-sx)**2 + (fy-sy)**2 <= fr**2:
                        
                        graph[out].append(ins)
        
        answer = defaultdict(int)
        for itr in range(len(bombs)):
            visited = set()
            self.dfs(graph,itr,visited)
            answer[itr]=len(visited)
            
        return max(answer.values())