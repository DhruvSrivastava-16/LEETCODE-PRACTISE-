"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if not node:
            return 
        s=None
        
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            
            return node
        
        else:
            while node.parent and node==node.parent.right:
                node = node.parent
                
            return node.parent
            
                
                
        return s
                
        