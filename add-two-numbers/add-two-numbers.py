# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        Head = ListNode()
        temp = Head
        carry = 0 
        val = 0
        t_sum = 0
        
        while l1 or l2:
            t_sum = 0 
            if l1:
                t_sum += l1.val
                l1 = l1.next
                
            if l2:
                t_sum += l2.val 
                l2 = l2.next
            
            t_sum+=carry
            carry = t_sum//10
            val = t_sum%10
            
            temp.next = ListNode(val)
            temp = temp.next
            
        
        if carry!=0:
            temp.next = ListNode(carry)
        
        return Head.next
            