# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque

class Solution:
    def bfs(self,root):
        if root is None:
            return []
        
        columnTable = defaultdict(list)
        
        visited = set()
        dq = deque()
        dq.append([root,0])
        visited.add(root)
        
        while dq:
            temp, c = dq.popleft()
            columnTable[c].append(temp.val)
            
            if temp.left:
                dq.append((temp.left,c-1))
                
            if temp.right:
                dq.append((temp.right,c+1))
                
        print(columnTable)
        return [columnTable[x] for x in sorted(columnTable.keys())]
        
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = defaultdict(list)
        answer = self.bfs(root)
        return answer
        