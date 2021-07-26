# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def successor(self,root):
        root = root.right
        while root.left:
            root = root.left
            
        return root
    
    def predecessor(self,root):
        root = root.left
        while root.right:
            root = root.right
            
        return root
                
                
                
                
                
                
                
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        if root.val>key:
            root.left = self.deleteNode(root.left,key)
            
        elif root.val<key:
            root.right = self.deleteNode(root.right,key)
            
        else:
            
            if (not root.left and not root.right):
                root = None
                
            elif root.right:
                suc = self.successor(root)
                root.val = suc.val
                root.right = self.deleteNode(root.right,root.val)
            
            else:
                pre = self.predecessor(root)
                root.val = pre.val
                root.left = self.deleteNode(root.left,root.val)
            
        return root
        