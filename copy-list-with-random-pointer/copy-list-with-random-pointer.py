"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    
    def helper(self, head):
        if not head:
            return None
        
        if head in self.visited:
            return self.visited[head]
        
        
        Node_t = Node(head.val,None,None)
        
        self.visited[head] = Node_t
        Node_t.next = self.helper(head.next)
        Node_t.random = self.helper(head.random)
        
        return Node_t
        
    
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        self.visited = {}
        return self.helper(head)