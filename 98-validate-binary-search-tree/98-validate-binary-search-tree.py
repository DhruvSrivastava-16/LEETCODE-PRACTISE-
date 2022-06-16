# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,node,sort):
        
        if node.left:
            self.helper(node.left,sort)
            
        sort.append(node.val)
        
        if node.right:
            self.helper(node.right,sort)        
        
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        sort = []
        self.helper(root, sort)
        for i in range(0,len(sort)-1):
            
            if sort[i+1] <= sort[i]:
                return False
            
        return True
            
        