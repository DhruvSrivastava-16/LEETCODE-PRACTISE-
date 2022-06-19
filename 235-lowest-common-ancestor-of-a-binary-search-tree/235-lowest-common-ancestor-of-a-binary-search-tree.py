# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def dfs(self,root,p,q):
        
        node = root
        p_val = p.val
        q_val = q.val
        parent_val = node.val
        
        if p_val > parent_val and q_val > parent_val:    
            # If both p and q are greater than parent
            node = node.right
            return self.dfs(node,p,q)
        elif p_val < parent_val and q_val < parent_val:
            # If both p and q are lesser than parent
            node = node.left
            return self.dfs(node,p,q)
        else:
            # We have found the split point, i.e. the LCA node.
            return node
        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Value of p
        return self.dfs(root,p,q)
        