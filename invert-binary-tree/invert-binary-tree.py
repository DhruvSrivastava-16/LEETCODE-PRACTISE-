# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def interchange(self,root):
        if not root:
            return 
        
        left = self.interchange(root.left)
        right = self.interchange(root.right)
        
        root.left, root.right = right,left
        
        return root
        
        
        #return self.interchange(r1.left,r2.right) and self.interchange(r1.right,r2.left)
    
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.interchange(root)
        return root
        