# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self,root,currMax,curr):
        if not root:
            return 
        
        curr = max(curr,root.val)
        currMax[(root.val,root)] = curr
        
        self.dfs(root.left,currMax,curr)
        self.dfs(root.right,currMax,curr)
        
    
    
    def goodNodes(self, root: TreeNode) -> int:
        
        currMax = defaultdict(list)
        curr = root.val
        self.dfs(root,currMax,curr)
        count = 0
        
        for k, v in currMax.items():
            if k[0]>=v:
                count+=1
                
        return count