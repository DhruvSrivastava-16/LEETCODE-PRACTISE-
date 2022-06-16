"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    
    def dfs(self,node,visited):
        if not node:
            return node
        
        if node in visited:
            return visited[node]
        
        newNode = Node(node.val)
        visited[node] = newNode
        
        for n in node.neighbors:
            newNode.neighbors.append(self.dfs(n,visited))
            
        return newNode
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = dict()
        return self.dfs(node,visited)