# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def trav(self,leafs,temp,root):
        if root is None:
            return 
        
        temp.append(str(root.val))
        
        if root.left is None and root.right is None:
            leafs.append(temp[:])
            return 
        if root.left:
            self.trav(leafs,temp,root.left)
            temp.pop()
        if root.right:
            self.trav(leafs,temp,root.right)
            temp.pop()
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        leafs, temp = [], []
        self.trav(leafs,temp,root)
        summ = 0
        for nums in leafs:
            if nums:
                number = int(''.join(nums))
                summ+=number
        
        return summ