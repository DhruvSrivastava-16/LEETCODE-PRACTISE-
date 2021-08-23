# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = []
    
    def helper(self,root,parent,temp):
        if root is None:
            return 
        
        if root.left is None and root.right is None:
            print(root)
            temp.append(root.val)
            if root == parent.left:
                parent.left = None
                
            else:
                parent.right = None
                
            root.val = 'LEAF'
            root = None
            print(root)
            
        else:
            print('A: ',root.val)
        
            self.helper(root.left,root,temp)
            self.helper(root.right,root,temp)
    
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans=[]
        temp = []
        while True:
            if root.left is None and root.right is None:
                self.ans.append([root.val])
                break
            self.helper(root,None,temp)
            self.ans.append(temp[:])
            temp = []
            
                
        return(self.ans)
        #(root)