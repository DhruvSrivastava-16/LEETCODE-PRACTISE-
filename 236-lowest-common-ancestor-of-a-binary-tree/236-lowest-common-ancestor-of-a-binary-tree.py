# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def dfs(self, root,pmap):
        if not root:
            return 
        
        if root.right:
            pmap[root.right]=root
            self.dfs(root.right,pmap)
        
        if root.left:
            pmap[root.left]=root
            self.dfs(root.left,pmap)
        
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        pmap = dict()
        pmap[root] = None
        self.dfs(root,pmap)
 
        
        ancestorsQ = []
        
        while q:
            ancestorsQ.append(q)
            q = pmap[q]
            
        ans = None
        
        while p:
            if p in ancestorsQ:
                return p
                
            p = pmap[p]
            
        return ans