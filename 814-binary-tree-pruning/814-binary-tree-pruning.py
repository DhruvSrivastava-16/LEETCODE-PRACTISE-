# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def containsOne(self,root):
        if not root:
            return False
        
        # if root.val!=1:
        #     return False
        
        left = self.containsOne(root.left)
        right = self.containsOne(root.right)
        
        if not left:
            root.left=None
            
        if not right:
            root.right=None
            
        return left or right or root.val==1
    
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        return root if self.containsOne(root) else None