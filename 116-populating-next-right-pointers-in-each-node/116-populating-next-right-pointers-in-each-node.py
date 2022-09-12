"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        levelMap = defaultdict(list)
        dq = deque()
        
        level = 0
        dq.append((root,level))
        
        while dq:
            
            node, level = dq.popleft()
            levelMap[level].append(node)
            
            if node.left:
                dq.append((node.left,level+1))
                
            if node.right:
                dq.append((node.right,level+1))
                
        for value in levelMap.values():
            
            for itr in range(1,len(value)):
                value[itr-1].next = value[itr]
                
            value[-1].next = None
            
            
        return root
        