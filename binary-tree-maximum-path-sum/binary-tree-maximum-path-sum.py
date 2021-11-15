# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        def maxGain(node):
            nonlocal maxsum
            
            if not node:
                return 0
            
            left_s = max(maxGain(node.left),0)
            right_s = max(maxGain(node.right),0)
            
            price = node.val + left_s + right_s 
            
            maxsum = max(maxsum, price)
            
            return node.val + max(left_s,right_s)
        
        maxsum = float('-inf')
        maxGain(root)
        return maxsum