# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderT(self,root,inorder):
        if not root:
            return 
        
        self.inorderT(root.left,inorder)
        inorder.append(root.val)
        self.inorderT(root.right,inorder)
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = []
        self.inorderT(root,inorder)
        return inorder[k-1]
        