# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        main = answer = ListNode()
        head2 = pivot = ListNode()
        while head:
            
            if head.val<x:
                
                answer.next = ListNode(head.val)
                answer = answer.next
                
            else:
                pivot.next = ListNode(head.val)
                pivot = pivot.next
                
            head = head.next
            
        print(answer,pivot)
        answer.next = head2.next
        
        return main.next
                
                
                
            
            
        