# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # print(slow.val)
        prev = None
        curr = slow
        
        while curr:
            
            tempNext = curr.next
            curr.next = prev
            prev = curr
            curr = tempNext
            
            
        while prev and head:
            
            if prev.val!=head.val:
                return False
            
            prev = prev.next 
            head = head.next 
            
        return True
            