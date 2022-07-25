# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self,node):
        
        if not node:
            return 
        
        if not node.left and not node.right:
            return node
        
        left = self.helper(node.left)
        right = self.helper(node.right)
        
        if left:
            left.right = node.right
            node.right = node.left
            node.left = None
            
        return right if right else left
        
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.helper(root)
        return root
        