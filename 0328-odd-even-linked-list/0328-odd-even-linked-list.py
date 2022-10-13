# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None):
            return None;
        main = head
        odd = head 
        even = head.next
        evenHead = even
        head = head.next
        
        while (head and head.next):
            odd.next = head.next;
            odd = odd.next;
            even.next = odd.next;
            even = odd.next;
            head = odd.next
        
        odd.next = evenHead;
        return main