# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,depth):
        
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            self.ans = min(self.ans,depth+1)
            return
        
            
        self.dfs(root.left,depth+1)
        self.dfs(root.right,depth+1)
    
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.ans = float('inf')
        self.dfs(root,0)
        return self.ans
    
    