"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def helper(self,head):
        if head is None:
            return None
        
        if head in self.visited:
            return self.visited[head]
        
        node = Node(head.val,None,None)
        
        self.visited[head] = node
        
        node.next = self.helper(head.next)
        node.random = self.helper(head.random)
        
        return node
            
    
    def copyRandomList(self, head: 'Node') -> 'Node':
        self.visited={}
        return self.helper(head)