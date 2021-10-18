# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict, deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        h_map = defaultdict(list)
        
        def dfs(root,h_map):
            if root is None:
                return 
            
            if root.left is not None:
                h_map[root.val].append(root.left.val)
                h_map[root.left.val].append(root.val)
                dfs(root.left,h_map)
                
            if root.right is not None:
                h_map[root.val].append(root.right.val)
                h_map[root.right.val].append(root.val)
                dfs(root.right,h_map)
                
        dfs(root,h_map)
        bfs_store = defaultdict(int)
        target = target.val
        
        def bfs(target,root,bfs_store):
            visited = set()
            dq = deque()
            
            dq.append((target,0))
            visited.add(target)
            bfs_store[target] = 0
            
            while dq:
                temp, dist = dq.popleft()
                
                for n in h_map[temp]:
                    if n not in visited:
                        dq.append((n,dist+1))
                        bfs_store[n]=dist+1
                        visited.add(n)
                    
        bfs(target,root,bfs_store)
        
        answer = []
        for i,v in bfs_store.items():
            if v==k:
                
                answer.append(i)
                
        return answer
                    
                
            
            
            
            
        