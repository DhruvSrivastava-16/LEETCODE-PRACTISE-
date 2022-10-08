"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def bfs(self,graph,node,hmap):
        
        dq = deque()
        visited = set()
        
        dq.append((node,0))
        visited.add(node)
        
        while dq:
            
            node, dist = dq.popleft()
            hmap[node] = dist
            
            for ne in graph[node]:
                
                if ne not in visited:
                    
                    dq.append((ne,dist+1))
                    visited.add(ne)
                    
    def trav(self,root,graph):
        if not root:
            return None
        
        for ne in root.children:
            graph[root].append(ne)
            graph[ne].append(root)
            self.trav(ne,graph)
            
        
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        
        graph = defaultdict(list)
        self.trav(root,graph)
        
        hmap = defaultdict(list)
        if len(graph.keys())==0:
            return 0
        node1 = list(graph.keys())[0]
        self.bfs(graph,node1,hmap)
        
        farthestNode = sorted(list(hmap.items()),key = lambda x:x[1])[-1][0]
        
        hmap = defaultdict(list)
        
        self.bfs(graph,farthestNode,hmap)
        
        return max(hmap.values())