class Solution:
       
    def isSameTree(self,s,t):
        if not s or not t:
            return not s and not t
        elif s.val==t.val:
            return (self.isSameTree(s.left,t.left) and self.isSameTree(s.right,t.right))
        else:
            return False
        
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:  
        if not s:
            return False
        elif self.isSameTree(s,t):
            return True
        else:
            return (self.isSubtree(s.left,t) or self.isSubtree(s.right,t))