# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def dfs(self,root,graph):
        if not root:
            return 
        
        if root.left:
            graph[root].append(root.left)
            graph[root.left].append(root)
            self.dfs(root.left,graph)
            
        if root.right: 
            graph[root].append(root.right)
            graph[root.right].append(root)
            self.dfs(root.right,graph)
            
        return 

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        self.dfs(root,graph)
        
        
        answer = []
        visited = set()
        dq = deque()
        
        dist = 0
        dq.append((target, dist))
        visited.add(target)
        
        while dq:
            
            node, dist = dq.popleft()
            
            if dist == k:
                answer.append(node.val)
                
            if dist>k:
                return answer
            
            for ne in graph[node]:

                if ne not in visited:
                    dq.append((ne,dist+1))
                    visited.add(ne)
                    
        return answer
                    
                
        