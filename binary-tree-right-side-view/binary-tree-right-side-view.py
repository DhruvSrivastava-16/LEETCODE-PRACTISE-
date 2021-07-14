# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def util(self,rightview, root):
        if not root:
            return []
        
        next_level = []
        
        next_level = [root]
        
        while next_level:
            
            curr_level = next_level
            next_level = []
            
            
            while curr_level:
                k = curr_level.pop(0)
                if(k.left):
                    next_level.append(k.left)

                if(k.right):
                    next_level.append(k.right)
            
            
            rightview.append(k.val)
            
        return(rightview)
                
        
    def rightSideView(self, root: TreeNode) -> List[int]:
        visited = {}
        rightview = []
        a=self.util(rightview,root)
        return rightview
        