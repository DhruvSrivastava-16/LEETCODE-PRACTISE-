# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trav(self,left,right):
        if not right and not left:
            return True
        if (left == None or right == None): 
            return False
    
    
        
        return  left.val==right.val and self.trav(left.left,right.right) and self.trav(left.right,right.left)
            

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.trav(root,root)
        