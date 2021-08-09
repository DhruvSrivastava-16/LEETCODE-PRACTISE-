# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def revLinkedList(self,l):
        curr = l
        prev = None
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
            
        return prev
    
    
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.revLinkedList(l1)
        l2 = self.revLinkedList(l2)
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
            print('Val',val)
            temp.next = ListNode(val)
            temp = temp.next
            
        
        if carry!=0:
            temp.next = ListNode(carry)
        ans = self.revLinkedList(Head.next)
        return ans