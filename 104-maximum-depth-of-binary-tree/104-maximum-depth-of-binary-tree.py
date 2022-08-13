# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,level):
        if not root:
            return 0
        
        left = self.dfs(root.left,level+1)
        right = self.dfs(root.right,level+1)
        
        return max(left,right)+1
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return self.dfs(root,1)