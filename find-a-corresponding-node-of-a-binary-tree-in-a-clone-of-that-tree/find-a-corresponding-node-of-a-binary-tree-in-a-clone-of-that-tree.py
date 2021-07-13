# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ans = None
    def inorder(self,root1,roo2,target):
        
        if not root1:
            return
        
        if root1 == target:
            self.ans = roo2
        
        self.inorder(root1.left,roo2.left,target)
        print(root1.val,roo2.val)
        self.inorder(root1.right,roo2.right,target)
        
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.ans = None
        self.inorder(original,cloned,target)
        return self.ans
        
        
        
        