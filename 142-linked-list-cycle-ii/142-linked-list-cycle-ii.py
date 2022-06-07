# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        seen = set()
        
        while slow:
            
            if slow in seen:
                return slow
            
            seen.add(slow)
            slow = slow.next
            
        