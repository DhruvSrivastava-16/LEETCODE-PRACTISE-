"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque, defaultdict

class Solution:
    def bfs(self,root):
        if root is None:
            return []
        
        bfs_map = defaultdict(list)
        bfs_map_v = defaultdict(list)

        dq = deque()
        dq.append((root,0))
        
        while dq:
            
            node, level = dq.popleft()
            bfs_map[level].append(node)
            bfs_map_v[level].append(node.val)
            
            if node.left:
                dq.append((node.left,level+1))
                
            if node.right:
                dq.append((node.right,level+1))
                
                
        print(bfs_map_v)
            
        for k,v in bfs_map.items():
            
            i = 0
            
            for i in range(len(v)-1):
                print('in',bfs_map[k][i].val,bfs_map[k][i+1].val)
                bfs_map[k][i].next = bfs_map[k][i+1]
                

            bfs_map[k][len(v)-1].next = None
        
    
    def connect(self, root: 'Node') -> 'Node':
        self.bfs(root)
        return root
        
        
        
        