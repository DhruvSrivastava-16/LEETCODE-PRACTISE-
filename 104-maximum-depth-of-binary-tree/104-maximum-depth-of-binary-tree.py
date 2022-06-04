# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, dp):
        # left, right = 0, 0
        if root is None:
            return 0
        
        # print(root.val)
        left = self.dfs(root.left, dp)
        right = self.dfs(root.right, dp)
        return max(left, right) + 1
        
        
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)