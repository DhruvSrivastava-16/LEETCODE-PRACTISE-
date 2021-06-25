# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self,root,sum_ans,low,high):
        if root is None:
            return sum_ans
        
        if root.val >= low  and root.val <= high:
            sum_ans = sum_ans + root.val
        
        print(root.val,sum_ans)
        
        sum_ans = self.traversal(root.left,sum_ans,low,high)
        sum_ans = self.traversal(root.right,sum_ans,low,high)
        
        return sum_ans
    
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        x = self.traversal(root,0,low,high)
        print (x)
        return x
        
        
        