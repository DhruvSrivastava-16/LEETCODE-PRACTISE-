# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    curIdx = 0
    def helper(self,preorder,inorder,curIdx,l,r):
        print(self.curIdx)
        if l>r or self.curIdx>=len(preorder):
            return None
        
        rootV = preorder[self.curIdx]
        root = TreeNode(rootV)
        self.curIdx+=1

        inorderLoc = inorder.index(rootV)
        
        root.left = self.helper(preorder,inorder,curIdx,l,inorderLoc-1)
        root.right = self.helper(preorder,inorder,curIdx,inorderLoc+1,r)
        
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.curIdx = 0
        
        return self.helper(preorder, inorder, 0,0, len(preorder)-1)