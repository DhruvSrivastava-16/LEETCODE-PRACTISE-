# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self,root):
        if not root:
            return None
        
        elif root.left is None and root.right is None:
            return root
        
        leftTail = self.helper(root.left)
        rightTail = self.helper(root.right)
        
        if leftTail:
            
            leftTail.right = root.right
            root.right = root.left 
            root.left = None
            
        return rightTail if rightTail else leftTail
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.helper(root)
        return root