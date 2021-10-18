# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict

class Solution:
    def bfs(self,root):
        if not root:
            return None
        
        
        visited =  defaultdict(bool)
        dq = deque()
        level = 0
        
        visited[root] = True
        dq.append([root,level])
        h_map = defaultdict(list)
        
        while dq:
            
            temp, level  = dq.popleft()
            h_map[level].append(temp.val)
            
            print(temp.val)
            
            if temp.left is not None:
                dq.append([temp.left,level+1])
                
            if temp.right is not None:
                dq.append([temp.right,level+1])
        
        return (h_map)
    
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        h_map = self.bfs(root)
        answer = []
        
        if h_map is None:
            return []
        
        for v in h_map.values():
            if len(v)<1:
                return [] 
            
            answer.append(max(v))
            
        return answer
        