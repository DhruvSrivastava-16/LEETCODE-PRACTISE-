# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def is_same(self,r,sr) -> bool:
        if not r and not sr:
            return True
        if r and sr and r.val == sr.val:
            return (self.is_same(r.left, sr.left) 
                    and self.is_same(r.right, sr.right))
        return False
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot:
            return True
        
        if not root:
            return False
        
        if self.is_same(root,subRoot):
            return True
        
        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)