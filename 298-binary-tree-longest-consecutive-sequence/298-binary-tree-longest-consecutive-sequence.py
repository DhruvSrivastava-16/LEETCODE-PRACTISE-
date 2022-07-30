# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self,root,length,parent):
        if not root:
            return length
        
        if parent and parent.val+1==root.val:
            length+=1
            
        else:
            length = 1
            
        return max(length,max(self.dfs(root.left,length,root),self.dfs(root.right,length,root)))
    
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        a = self.dfs(root,0,None)
        return(a)