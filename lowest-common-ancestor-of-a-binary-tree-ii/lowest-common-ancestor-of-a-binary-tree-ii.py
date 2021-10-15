# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def lca(node):
            if not node:
                return False

            left = lca(node.left)
            right = lca(node.right)
            current = node.val in [p.val, q.val]
            
            if (left and right) or (current and (left or right)):
                lca_node[0] = node
            
            return left or right or current
        
        lca_node = [None]
        lca(root)
        return lca_node[0]