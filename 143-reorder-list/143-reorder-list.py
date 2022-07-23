# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def findMiddle(self,head):
        
        if not head:
            return 
        
        slow = head
        fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        return slow
    
    
    def reverseLinkedList(self,head):
        
        prev = None
        itr = head
        
        while itr:
            
            temp = itr.next
            itr.next = prev
            prev = itr
            itr = temp 
            
            
        return (prev)
        
        
    def mergeLinkedList(self,head1,head2):
        
        first = head1
        second = head2
        
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
            
        return (head1)
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        middle = self.findMiddle(head)
        middle = self.reverseLinkedList(middle)

        return self.mergeLinkedList(head,middle)