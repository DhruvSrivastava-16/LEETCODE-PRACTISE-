# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    newroot = []
    def inorder(self,root):
        temp = TreeNode(None)
        if root is None:
            return 
        
        self.inorder(root.left)
        
        self.newroot.append(root)
        
        self.inorder(root.right)
        
        
        
    
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        
        self.newroot = []
        self.inorder(root)
        print(self.newroot)
        ans = temp = TreeNode(None)
        temp = ans
        for i in self.newroot:
            temp.right = TreeNode(i.val)
            temp = temp.right
            
        return ans.right
        
        
        