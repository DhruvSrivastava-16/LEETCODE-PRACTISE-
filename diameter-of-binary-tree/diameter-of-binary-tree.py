# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxheight(self,root):
        if root is None: 
            return 0
        
        
        return 1+ max(self.maxheight(root.left),self.maxheight(root.right)) 
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        mh_l = self.maxheight(root.left)
        mh_r = self.maxheight(root.right)
        
        ldia = self.diameterOfBinaryTree(root.left)
        rdia = self.diameterOfBinaryTree(root.right)
        
        return max(mh_l + mh_r,max(ldia,rdia))
        