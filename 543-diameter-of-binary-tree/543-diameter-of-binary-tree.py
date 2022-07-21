# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def trav(self,root):
        if not root:
            return 0
        global dia
        
        l = self.trav(root.left)
        r = self.trav(root.right)
        dia = max(dia,l+r)
        
        return max(l,r)+1
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global dia
        dia = 0
        self.trav(root)
        return dia