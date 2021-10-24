# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def bfs(self,root):
        if root is None:
            return 0
        
        count = 0
        
        visited = set()
        dq = deque()
        dq.append(root)
        
        while dq:
            
            temp = dq.popleft()
            count+=1
            
            print(temp.val)
                
            if temp.left and temp.left not in visited:
                visited.add(temp.left)
                
                dq.append(temp.left)
                
            if temp.right and temp.right not in visited:
                visited.add(temp.right)

                dq.append(temp.right)
                
        return count
            
            
            
        
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.bfs(root)