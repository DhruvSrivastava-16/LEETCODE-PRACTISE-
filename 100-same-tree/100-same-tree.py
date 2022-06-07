# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def match(self,p,q):
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val!=q.val:
            return False
        
        return self.match(p.left,q.left) and self.match(p.right,q.right)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.match(p,q)