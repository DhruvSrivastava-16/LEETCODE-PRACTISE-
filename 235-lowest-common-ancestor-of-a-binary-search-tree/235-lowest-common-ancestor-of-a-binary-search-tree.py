# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def dfs(self,root,p,q):
  
        node = root 
        parv = node.val
        
        qv = q.val
        pv = p.val
        
        if parv > qv and parv > pv:
            return self.dfs(node.left,p,q)
        
        elif parv<qv and parv<pv:
            return self.dfs(node.right,p,q)
        
        else:
            return root
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        return self.dfs(root,p,q)
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
    
#     def dfs(self,root,p,q):
        
#         node = root
#         p_val = p.val
#         q_val = q.val
#         parent_val = node.val
        
#         if p_val > parent_val and q_val > parent_val:    
#             return self.dfs(node.right,p,q)
#         elif p_val < parent_val and q_val < parent_val:
#             return self.dfs(node.left,p,q)
#         else:
#             return node
        
#     def lowestCommonAncestor(self, root, p, q):
#         """
#         :type root: TreeNode
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: TreeNode
#         """

#         # Value of p
#         return self.dfs(root,p,q)
        

        