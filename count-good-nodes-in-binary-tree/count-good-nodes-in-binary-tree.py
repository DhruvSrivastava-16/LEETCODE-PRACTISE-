# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
           
        cm = []
        self.tr(root,cm,root,root.val)
        print(cm)
        ans = 0
        for i in cm:
            if i[0] >= i[1]:
                ans += 1
                
        return ans
  
    def tr(self,root,cm,mr,tmax = -1):
        if root is None:
            
            return 
        
        
        
        
        if root.val >= tmax:
            tmax = root.val
            
        
        cm.append((root.val,tmax))
        
        
       # print (root.val, cm)
            
        
        self.tr(root.left,cm,mr,tmax)
        self.tr(root.right,cm,mr,tmax)
        
