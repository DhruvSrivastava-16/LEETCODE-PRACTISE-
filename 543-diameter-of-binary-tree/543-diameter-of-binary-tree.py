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
        
        l = self.trav(root.left)
        r = self.trav(root.right)
        self.dia = max(self.dia,l+r)
        
        return max(l,r)+1
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia = 0
        self.trav(root)
        return self.dia