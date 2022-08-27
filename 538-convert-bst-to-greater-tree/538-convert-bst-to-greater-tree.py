# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.total = 0
        
    def dfs(self,root):
        if root is not None:
            self.dfs(root.right)
            self.total += root.val
            root.val = self.total
            self.dfs(root.left)
            
        return root
            
    
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        return self.dfs(root)
        