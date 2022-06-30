# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trim(self,root):
        if not root:
            return None
        
        elif root.val<self.low:
            return self.trim(root.right)
        
        elif root.val>self.high:
            return self.trim(root.left)
        
        else:
            root.left = self.trim(root.left)
            root.right = self.trim(root.right)
        
        
            return root
            
            
    
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        self.low = low
        self.high = high
        return self.trim(root)