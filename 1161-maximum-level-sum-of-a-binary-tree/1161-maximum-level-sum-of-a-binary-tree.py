# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict
class Solution:
    
    def bfs(self,lmap,root,level):
        dq = deque()
        dq.append((root,level))
        
        while dq:
            
            node, l = dq.popleft()
            lmap[l].append(node.val)
            
            if node.left:
                dq.append((node.left,l+1))
            
            if node.right:
                dq.append((node.right,l+1))
    
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        lmap = defaultdict(list)
        self.bfs(lmap,root,1)
        
        maxx = -float('inf')
        ans = None
        
        for k,v in lmap.items():
            if sum(v)>maxx:
                ans = k
                maxx = sum(v)
                
        return ans