# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    total = 0 
   
    ''' 
    def greaterVal(self,root) -> int:
        
        if root is None:
            return 0
        
        return root.val + self.greaterVal(root.right)
        
        
    
    def makeGreater(self,root):
        
        if root is None:
            return 0
        
       # if root.left is None and root.right is None:
        #    return root.val
        
    '''    
    
        
        
    
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        
        self.convertBST(root.right)
        self.total = self.total + root.val
        root.val = self.total
        self.convertBST(root.left)
        
        return root
        