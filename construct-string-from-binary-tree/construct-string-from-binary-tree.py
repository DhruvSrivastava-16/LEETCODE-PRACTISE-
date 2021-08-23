# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def help(self,root):
        if root is None:
            return ''
        
        if root.left is None and root.right is None:
        
            return str(root.val)
        
        if root.right is None:
            return str(root.val) + '(' + self.help(root.left)+')'
        
    
        
        return str(root.val) + '('+self.help(root.left) +')'+'('+ self.help(root.right)+')'
                                                               
        
    def tree2str(self, root: Optional[TreeNode]) -> str:
        a=self.help(root)
        return(a)