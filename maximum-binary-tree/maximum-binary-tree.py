# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        root = TreeNode(max(nums))
        max_loc = nums.index(max(nums))
        root.left = self.constructMaximumBinaryTree(nums[:max_loc])
        root.right = self.constructMaximumBinaryTree(nums[max_loc+1:])
        return root
        
        