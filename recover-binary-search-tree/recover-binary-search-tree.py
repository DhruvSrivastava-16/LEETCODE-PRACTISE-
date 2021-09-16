# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root):
        if not root:
            return 
        
        self.inorder(root.left)
        self.inord.append(root)
        self.inorder(root.right)
    
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        self.inord = []
        self.inorder(root)
        
        err1 = False
        err2 = False
        
        for i in self.inord:
            print(i.val,end=" ")
        
        for i in range(0,len(self.inord)-1):
            if self.inord[i].val > self.inord[i+1].val:
                err1 = self.inord[i+1].val
                
                
                if not err2:
                    err2 = self.inord[i].val
                else:
                    break
        
        print(err1,err2,"\n")
                
        for i in self.inord:
            if i.val == err2:
                i.val = err1
                continue
            
            if i.val == err1:
                i.val = err2
                
        for i in self.inord:
            print(i.val,end=" ")
    
        
