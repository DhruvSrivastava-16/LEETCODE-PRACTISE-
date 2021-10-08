class Solution:

    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        adj_list = collections.defaultdict(list)
        
        def build_graph():
            for node1,node2 in adjacentPairs:
                adj_list[node1].append(node2)
                adj_list[node2].append(node1)
                
                
        build_graph()
        
        def find_start_node():
            for node,values in adj_list.items():
                if len(values) == 1:
                    return(node)
            
        start_node = find_start_node()
        visited = set()
        path = []
        
        def dfs(node):
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor)
            
            path.append(node)
        
        dfs(start_node)
        return(path)