# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self,answer,node,deleteSet,parent,direction):
        if not node:
            return 

        self.dfs(answer,node.left,deleteSet,node,'L')
        self.dfs(answer,node.right,deleteSet,node,'R')
        
        if node.val in deleteSet:
            if parent:
                if direction=='L':
                    parent.left = None
                else:
                    parent.right = None

            if node.right:
                answer.append(node.right)

            if node.left:
                answer.append(node.left)
    
            
            
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        deleteSet = set(to_delete)
        answer = []
        parent = None
        
        self.dfs(answer,root,deleteSet,parent,None)
        
        if root.val not in deleteSet:
            answer.append(root)
        
        return answer
