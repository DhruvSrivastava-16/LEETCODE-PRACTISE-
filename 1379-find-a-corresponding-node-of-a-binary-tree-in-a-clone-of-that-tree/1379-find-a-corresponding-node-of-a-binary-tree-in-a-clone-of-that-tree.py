# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self,clNode,target,ans):
        print(clNode.val,target.val)
        if clNode and clNode.val == target.val:
            ans.append(clNode)
            return 
        
        if clNode.left:
            self.dfs(clNode.left,target,ans)
            
        if clNode.right:
            self.dfs(clNode.right,target,ans)
        
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        ans = []
        
        self.dfs(cloned,target,ans)
        
        return ans[0]