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
        print(node,p_val,q_val,parent_val)
        
        if p_val > parent_val and q_val > parent_val:    
            # node = node.right
            return self.dfs(node.right,p,q)
        elif p_val < parent_val and q_val < parent_val:
            # node = node.left
            return self.dfs(node.left,p,q)
        else:
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
        