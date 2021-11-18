# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode):
       
        if not root:
            return True
        
        if not root.left and not root.right:
            return True
                
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        
        
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(left_height - right_height) <= 1
        
    def height(self,root):
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        left = self.height(root.left)
        
        right = self.height(root.right)
        
        return max(left, right) + 1
        
        
        
        
        