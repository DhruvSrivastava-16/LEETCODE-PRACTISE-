# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def traversal(self,root,hmap,layer):
        leftlayer, rightlayer = 0, 0
        if root is None:
            return 
        
        if root.left:
            leftlayer = self.traversal(root.left, hmap, layer)
        
        if root.right:
            rightlayer = self.traversal(root.right, hmap, layer)
            
        layer = max(leftlayer, rightlayer)
            
        hmap[layer].append(root.val)
            
        return layer + 1
        
    
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        hmap = collections.defaultdict(list)
        self.traversal(root, hmap, 0)
        
        return [value for key, value in hmap.items()]
        