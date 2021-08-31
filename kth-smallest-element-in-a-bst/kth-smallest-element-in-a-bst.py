# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root):
        if root is None:
            return 
        
        self.inorder(root.left)
        self.trav.append(root.val)
        self.inorder(root.right)
        
    
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if root is None:
            return 
        
        self.trav = []
        self.inorder(root)
        
        print(self.trav)
        return self.trav[k-1]