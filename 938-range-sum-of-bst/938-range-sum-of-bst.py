# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self, root, low, high):
        summ, left, right = 0, 0, 0
        if root is None:
            return 
        
        if root.val >= low and root.val <= high:
            summ += root.val
            
        if root.left:
            
            left = self.traversal(root.left, low, high)
            
        if root.right:
            
            right = self.traversal(root.right, low, high)
            
        return summ + left + right
            
            
    
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.traversal(root, low, high)