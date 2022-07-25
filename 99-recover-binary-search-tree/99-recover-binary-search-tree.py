# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        dq = []
        prev = x = y  = None
        
        while dq or root:
            while root:
                dq.append(root)
                root = root.left
                
            root = dq.pop()
            
            if prev and prev.val>root.val:
                y = root
                if x is None:
                    x = prev
                    
                else:
                    break
                    
            prev = root
            root = root.right
            
        x.val, y.val = y.val, x.val
                
        
        