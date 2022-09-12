class Solution:
    
    def dfs(self,node,graph,killed):
        
        killed.append(node)
        for ne in graph[node]:
            self.dfs(ne,graph,killed)
    
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        hmap = defaultdict(list)
        for itr in range(len(ppid)):
            hmap[ppid[itr]].append(pid[itr])
            
        killed = []
        
        # killed.append(kill)
        
        self.dfs(kill,hmap,killed)
            
        return killed
        