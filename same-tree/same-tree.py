# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self,root,dfs):
        if root is None:
            dfs.append(None)
            return 
        
        dfs.append(root.val)
        self.DFS(root.left,dfs)
        self.DFS(root.right,dfs)
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        temp = []
        self.DFS(p,temp)
        
        temp2 = []
        self.DFS(q,temp2)
        
        return temp==temp2
