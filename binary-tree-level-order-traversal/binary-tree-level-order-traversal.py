# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



def height(root):          #finds the height of the tree
    if not root:
        return 0
    
    else:
        lh = height(root.left)
        rh = height(root.right)
        
        if lh<rh:
            return rh+1
        
        else:
            return lh+1
    
def printlevel(root,level,l):
    
    if root is None:
        return 
    
    if level == 1:
        print(root.val)
        l.append(root.val)
        
    elif level>1:
        printlevel(root.left,level-1,l)
        printlevel(root.right,level-1,l)
        
    return l
        
        

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
   
        h = height(root)
    
        for i in range(1,h+1):
            l = printlevel(root,i,[])
            ans.append(l)
        
        return ans