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
        self.inorder_ar.append(root.val)
        self.inorder(root.right)
    
    def balancedTree(self,arr):
        if not arr:
            return 
        
        mid = len(arr)//2
        root = TreeNode(arr[mid])
        root.right = self.balancedTree(arr[mid+1:])
        root.left = self.balancedTree(arr[:mid])
        return root
        
        
    
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.inorder_ar = []
        self.inorder(root)
        print(self.inorder_ar)
        root = self.balancedTree(self.inorder_ar)
        return root
        
        
        