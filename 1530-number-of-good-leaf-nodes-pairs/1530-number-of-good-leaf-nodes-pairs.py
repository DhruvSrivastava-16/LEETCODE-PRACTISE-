# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def dfs(self,root,graph,leaves):
        if not root:
            return 
        
        if not root.left and not root.right:
            leaves.add(root)
            return 
        
        if root.right:
            graph[root].append(root.right)
            graph[root.right].append(root)
            self.dfs(root.right,graph,leaves)

        if root.left:
            graph[root].append(root.left)
            graph[root.left].append(root)
            self.dfs(root.left,graph,leaves)
            
    def bfs(self,node,graph,leaves,answer,distance):
        dq = deque()
        dist = 0
        
        dq.append((node,dist))
        visited = set()
        visited.add(node)
        
        while dq:
            n, dist = dq.popleft()
                    
            for ne in graph[n]:
                if ne not in visited:
                    
                    if ne in leaves and dist+1<=distance:
                        answer.append(1)
                        
                    dq.append((ne,dist+1))
                    visited.add(ne)
    
        
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        graph = defaultdict(list)
        leaves = set()
        
        self.dfs(root, graph,leaves)
        answer = []
        for node in leaves:
            visited = set()
            self.bfs(node,graph,leaves,answer,distance)
        
        return sum(answer)//2
        