# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self,node,par,covered):
        global answer
        
        if node:
            self.dfs(node.left,node,covered)
            self.dfs(node.right,node,covered)
            if (par is None and node not in covered or
                        node.left not in covered or node.right not in covered):
                    answer += 1
                    covered.update({node, par, node.left, node.right})

        
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        global answer
        answer = 0
        covered = {None}
        par = None
        self.dfs(root,par,covered)
        return answer