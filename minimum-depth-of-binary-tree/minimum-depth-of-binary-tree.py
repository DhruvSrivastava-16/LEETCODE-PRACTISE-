# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        lh = float('inf')
        rh = float('inf')
        if root.left:
            lh=self.minDepth(root.left)
        if root.right:
            rh=self.minDepth(root.right)
            
        m = min(lh,rh)
        
        return m+1