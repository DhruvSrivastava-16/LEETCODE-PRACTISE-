# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited = {}
        cycle = 0 
        while head:
            if head not in visited:
                visited[head]=1
                
            else:
                cycle = 1
                break
                
            head = head.next
            
        if cycle==1:
            return True
        
        return False
        
        