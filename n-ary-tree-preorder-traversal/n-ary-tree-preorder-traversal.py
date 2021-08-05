"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def helper(self,root,ans):
        if not root:
            return 
        
        ans.append(root.val)
        self.helper(root.children,ans)
        
        
    def preorder(self, root: 'Node') -> List[int]:
        if not root: 
            return 
        
        
        ans = []
        dq = deque()
        dq.append(root)
        while dq:
            temp = dq.popleft()
            ans.append(temp.val)
            for i in temp.children[::-1]:
                dq.appendleft(i)
            
        return(ans)
    
        
        