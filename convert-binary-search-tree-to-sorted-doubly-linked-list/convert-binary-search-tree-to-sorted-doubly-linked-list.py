"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def left_last_func(self,root):
        if root is None:
            return None
        
        while root.right.val > root.val:
            root = root.right
            
        return root
    
    
    def right_first_func(self,root):
        if root is None:
            return None
            
        while root.left.val<root.val:
            root = root.left
        
        return root
            
    
    def inorder(self,root):
        if root is None:
            return None
        
        self.inorder(root.left)
        
        left_last = self.left_last_func(root.left)
        root.left  = left_last
        
        if left_last is not None:
            left_last.right = root
        
        self.inorder(root.right)
        right_first = self.right_first_func(root.right)
        
        if right_first is not None:
            right_first.left = root
        
        root.right = right_first
        
        head = self.right_first_func(root.left)
        tail = self.left_last_func(root.right)
        
        if head is None:
            head = root
            
        
        if tail is None:
            tail = root
            
        head.left = tail
        
            
        tail.right = head
        
        return head
        
    
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        return self.inorder(root)
        