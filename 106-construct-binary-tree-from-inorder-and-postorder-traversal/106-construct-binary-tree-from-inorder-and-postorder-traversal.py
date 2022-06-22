# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    idx = 0
    
    def helper(self,ino,pos,l,r):
        if l>r or self.idx<0:
            return None
        
        rv = pos[self.idx]
        rvl = ino.index(rv)
        root = TreeNode(rv)
        
        self.idx-=1
        
        root.right = self.helper(ino,pos,rvl+1,r)

        root.left = self.helper(ino,pos,l,rvl-1)
        
        return root
        
        
        
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.idx = len(postorder)-1
        return self.helper(inorder,postorder,0,len(inorder)-1)
        