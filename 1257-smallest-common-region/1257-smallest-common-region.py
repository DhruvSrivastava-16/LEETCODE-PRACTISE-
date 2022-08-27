class Solution:
    
    def dfs(self,visited,ancestor,graph,node):
        visited.add(node)
        
        for ne in graph[node]:
            if ne not in visited:
                ancestor[ne] = node
                self.dfs(visited,ancestor,graph,ne)
    
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        
        graph = defaultdict(list)
        
        for region in regions:
            
            graph[region[0]] += region[1:]
            
        ConnectedComponents = []
        ancestors = []
        visited = set()
        itr = 0
        for node in list(graph.keys()):
            ancestor = {node:None}
            
            
            if node not in visited:
                itr+=1
                self.dfs(visited,ancestor,graph,node)
            
                ancestors.append(ancestor)
            
        ancestor = ancestors[0]
        
        ancestorRegion1 = set()
        
        Itr = region1
        while Itr:
            ancestorRegion1.add(Itr)
            Itr = ancestor[Itr]
            
            
        while True:
            
            if region2 in ancestorRegion1:
                return region2
            
            region2 = ancestor[region2]