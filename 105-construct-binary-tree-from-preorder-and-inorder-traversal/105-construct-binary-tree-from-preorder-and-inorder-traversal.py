# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def builder(self,preorder,inorder,left,right):
        if left>right or self.index>=len(preorder):
            return 
        
        node = TreeNode(preorder[self.index])
        loc = inorder.index(preorder[self.index])
        self.index+=1
        node.left = self.builder(preorder,inorder,left,loc-1)
        node.right = self.builder(preorder,inorder,loc+1,right)
        
        return node
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        self.index = 0
        node = self.builder(preorder,inorder,0,len(preorder)-1)
        return node