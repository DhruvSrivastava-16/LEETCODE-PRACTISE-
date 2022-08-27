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
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return 
        
        dq = deque()
        dq.append((root,0))
        hmap = defaultdict(list)
        level = 0
        
        
        
        while dq:
            
            node, level = dq.popleft()
            
            hmap[level].append(node)
            
            if node.left:
                dq.append((node.left,level+1))
                
            if node.right:
                dq.append((node.right,level+1))
                
        for v in hmap.values():
            
            for itr in range(len(v)-1):
                v[itr].next = v[itr+1]
                
            v[-1].next = None
            
        return root