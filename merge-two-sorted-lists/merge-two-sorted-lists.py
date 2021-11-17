# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        itr = merged
         
        while l1 and l2:
            
            if l1.val < l2.val:
                itr.next = ListNode(l1.val)
                l1 = l1.next
                
            else:
                itr.next = ListNode(l2.val)
                l2 = l2.next
                
            itr = itr.next
            
        while l1:
            itr.next = ListNode(l1.val)
            itr = itr.next
            l1 = l1.next
            
        while l2:
            itr.next = ListNode(l2.val)
            itr = itr.next
            l2 = l2.next
            
        return merged.next