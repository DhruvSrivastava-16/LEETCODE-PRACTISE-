# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        main = ListNode(-1)
        main.next = head
        prev = main
        
        while head and head.next:
            
            first = head
            second = head.next
            prev.next = second 
            
            first.next = second.next
            second.next = first
            
            prev = first
            head = first.next
            
        return main.next
            