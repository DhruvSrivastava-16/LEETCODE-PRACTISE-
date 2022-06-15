# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    arr = []
    
    def dfs(self,node,parent,grandparent):
        
        if node and grandparent and grandparent.val%2==0:
            self.arr.append(node.val)
            
        grandparent = parent
        parent = node
        
        if node.left:
            self.dfs(node.left,parent,grandparent)
            
        if node.right:
            self.dfs(node.right,parent,grandparent)
    
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.arr = []
        grandparent = None
        parent = None
        self.dfs(root,parent,grandparent)
        return sum(self.arr)