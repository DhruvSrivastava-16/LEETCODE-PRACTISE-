# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,val):
        if root is None:
            root = TreeNode(val)
            return root
        
        temp = root
        newnode = TreeNode(val)
        
        while True:
            if temp.val > val and temp.left is not None:
                temp = temp.left
                
            if val >= temp.val and temp.right is not None:
                temp = temp.right
                
            if val < temp.val  and temp.left is None:
                temp.left = newnode
                break
            
            if val >= temp.val and temp.right is None:
                temp.right = newnode
                break
                
        return root
                
                
        
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    
        root = self.helper(root,val)
        return root