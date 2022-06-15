# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def buildTree(self,nums):
        if not nums or len(nums)==0:
            return None
        
        mid = nums.index(max(nums))

        rootNode = TreeNode(nums[mid])
        rootNode.left = self.buildTree(nums[:mid])
        rootNode.right = self.buildTree(nums[mid+1:])
        return rootNode
    
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.buildTree(nums)