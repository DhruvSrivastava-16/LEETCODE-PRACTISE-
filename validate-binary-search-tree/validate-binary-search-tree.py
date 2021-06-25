# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = []
    def inorder(self,root):
        if root is None:
            return 
        
        self.inorder(root.left)
        self.ans.append(root.val)
        self.inorder(root.right)
        
        
    
    def isValidBST(self, root: TreeNode) -> bool:
    
        self.ans = []
        
        self.inorder(root)
        print(len(self.ans))
        if len(self.ans) == 1:
            return True 
        
        for i in range(0,len(self.ans)-1):
            if self.ans[i] >= self.ans[i+1]:
                return False
            
        return True