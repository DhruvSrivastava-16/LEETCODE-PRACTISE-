# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self,s,temp,answer,root,curSum):
        if not root:
            return 
        
        if not root.left and not root.right:
            if curSum==s:
                answer.append(temp[:])
                return 
                
        if root.left:
            temp.append(root.left.val)
            self.dfs(s,temp,answer,root.left,curSum+root.left.val)
            temp.pop()
        
        if root.right:
            temp.append(root.right.val)
            self.dfs(s,temp,answer,root.right,curSum+root.right.val)
            temp.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        answer = []
        temp = []
        if root is None:
            return []
        temp.append(root.val)
        self.dfs(targetSum,temp,answer,root,root.val)
        return(answer)