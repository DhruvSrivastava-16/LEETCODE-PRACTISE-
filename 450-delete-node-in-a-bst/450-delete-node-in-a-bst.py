# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # One step right and then always left
    def successor(self, root: TreeNode) -> int:
            root = root.right
            while root.left:
                root = root.left
            return root.val
        
    # One step left and then always right
    def predecessor(self, root: TreeNode) -> int:
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        if key>root.val:
            root.right = self.deleteNode(root.right,key)
            
        elif key<root.val:
            root.left = self.deleteNode(root.left,key)
            
        else:
            
            if not root.left and not root.right:
                root = None
                
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right,root.val)
                
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
                
        return root

        
        