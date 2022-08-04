# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self,root):
        if not root:
            return 0
        
        global maxPath
        left = max(self.dfs(root.left),0)
        right = max(self.dfs(root.right),0)
        maxPath = max(maxPath,root.val+left+right)
        
        return root.val + max(left,right)
        
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global maxPath
        maxPath = float('-inf')
        self.dfs(root)
        return maxPath