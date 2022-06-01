# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict


class Solution:

    def traversal(self,root,level,hmap):
        if root is None:
            return 
        hmap[level].append(root.val)
        self.traversal(root.left,level+1,hmap)
        self.traversal(root.right,level+1,hmap)    
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        hmap = defaultdict(list)
        level = 0
        self.traversal(root,0,hmap)
        return [v[-1] for k,v in hmap.items()]
        


    

        