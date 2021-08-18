# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        
        prev = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        return(prev)
    
    
    def reach_middle(self,head):
        slow = head
        fast = head
        
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return(slow)
    
    def merge(self,head,rev_head):
        first = head
        second = rev_head
        while second.next:
            temp = first.next
            first.next = second
            first = temp
            
            temp = second.next
            second.next = first
            second = temp
             
        #print(head)
            
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #print("HEAD: ",head)
        mid = self.reach_middle(head)
        rev_mid = self.reverse(mid)
        self.merge(head,rev_mid)
        #print("HEAD: ",head)
        #print("Rev_Mid: ",rev_mid)