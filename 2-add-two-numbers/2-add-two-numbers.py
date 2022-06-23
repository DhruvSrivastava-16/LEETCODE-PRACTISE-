# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numGen(self,l):
        
        num = ''
        while l:
            num+=str(l.val)
            l = l.next
            
        return int(num[::-1])
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        num1 = self.numGen(l1)
        num2 = self.numGen(l2)
        summ = num1+num2
        summ = str(summ)
        summ = summ[::-1]
        head = ListNode()
        temp = head
        
        for i in summ:
            Nodee = ListNode(i)
            temp.next = Nodee
            temp = Nodee
            
        return head.next
            