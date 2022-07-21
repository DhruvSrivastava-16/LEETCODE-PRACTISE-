# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def diameter(self,root):
        if not root:
            return 0
        global dia
        left = self.diameter(root.left)
        right = self.diameter(root.right)
        dia = max(dia,left+right)
        
        return 1+max(left,right)
        
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        global dia
        dia = 0
        self.diameter(root)
        return dia