"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def nav_first(self,root):
        if root is None:
            return 
        
        while root.left.val<root.val:
            root = root.left
        
        return root
        
    
    def nav_last(self,root):
        if root is None:
            return 
        
        while root.right.val>root.val:
            root = root.right
        
        return root
        
    
    def inorder(self,root):
        if root is None:
            return 
        
        self.inorder(root.left)
        #reached the left most node
        left_last_node = self.nav_last(root.left)
        root.left = left_last_node
        
        if left_last_node is not None:
            left_last_node.right = root
        
        #self.root.right = parent
        self.inorder(root.right)
        right_first_node = self.nav_first(root.right)
        root.right = right_first_node
        
        if right_first_node is not None:
            right_first_node.left = root
        
        head = self.nav_first(root.left)
        tail = self.nav_last(root.right)
        
        if head is None:
            head = root
        
        if tail is None:
            tail = root    
            
        tail.right = head
        head.left = tail
        
        return head
        
        
        
        
        
    
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        root = self.inorder(root)
        return root