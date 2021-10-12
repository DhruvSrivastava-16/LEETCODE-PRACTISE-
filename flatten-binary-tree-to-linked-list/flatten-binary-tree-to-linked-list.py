# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        
        node = root
        
        while node:
            
            if node.left:
                
                right_most = node.left
                while right_most.right:
                    right_most = right_most.right
                    
                right_most.right = node.right
                node.right = node.left
                node.left = None
                
            node = node.right
            
            
        return node