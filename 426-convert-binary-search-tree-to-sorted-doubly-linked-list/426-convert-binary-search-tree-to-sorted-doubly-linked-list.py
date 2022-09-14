"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    
    head = None
    prev = None
    
    def dfs(self,node):
        if not node:
            return 
        
        self.dfs(node.left)
        
        if self.prev:
            
            node.left = self.prev
            self.prev.right = node
            
        else:
            self.head = node
            
        self.prev = node
        
        self.dfs(node.right)
    
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        self.dfs(root)
        self.prev.right = self.head
        self.head.left = self.prev
        
        return self.head