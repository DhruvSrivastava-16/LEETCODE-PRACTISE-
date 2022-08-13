# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def dfs(self,root,parents,parent):
        
        if not root:
            return 
        
        parents[root] = parent
        
        self.dfs(root.left,parents,root)
        self.dfs(root.right,parents,root)
        
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents  = {}
        parent = None
        self.dfs(root,parents,parent)
        
        ancestorsP = set()
        
        while p:
            ancestorsP.add(p)
            p = parents[p]
            
        while q:
            
            if q in ancestorsP:
                return q
            
            q = parents[q]