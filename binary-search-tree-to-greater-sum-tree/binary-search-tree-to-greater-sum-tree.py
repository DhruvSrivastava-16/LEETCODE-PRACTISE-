# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    cumsum = 0
    def modifiedtraversal(self,root,cumsum):
        
        if root is None:
            return 
        
        self.modifiedtraversal(root.right,self.cumsum);
        self.cumsum = self.cumsum + root.val
        root.val =  self.cumsum
        self.modifiedtraversal(root.left,self.cumsum);
        
        print(root.val)
        
        print(root.val)
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        self.cumsum = 0
        ans = root
        self.modifiedtraversal(root,self.cumsum)
        return ans
        