# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def check(self,p,q):
        if not p and q:
            return False
        
        if p and not q:
            return False
        
        if not p and not q:
            return True
        
        if p.val!=q.val:
            return False
        
        return self.check(p.left,q.left) and self.check(p.right,q.right)
    
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        return self.check(p,q)