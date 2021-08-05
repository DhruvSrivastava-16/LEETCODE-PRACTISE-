"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        
        dq = []
        
        ans = []
        dq.append(root)
        while dq:
            t = dq.pop()
            if t is not None:
                ans.append(t.val)
            
            
            for i in t.children:
                dq.append(i)
        
        return(ans[::-1])
            
            
        