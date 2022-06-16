# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        #find the mid
        slow = head
        fast = head
        
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
        
        
        #reverse a linked list
        prev = None
        
        while slow:
            
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            
        
        
        main = head

        first, second = head, prev
        
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
            
        
        return main
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            