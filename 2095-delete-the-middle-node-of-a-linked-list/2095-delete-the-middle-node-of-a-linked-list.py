# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        slow, fast = head, head
        
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
            
        print(slow.val)
        
        if slow.next:
            
            slow.val = slow.next.val
            slow.next = slow.next.next
            return head
        
        else:
            
            if head.next:
                head.next = None
                return head
            
            else:
                head = None
                return head
        
