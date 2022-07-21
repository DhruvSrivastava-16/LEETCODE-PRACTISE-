# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        count = 1
        left = None
        right = None
        
        itr = list1
        
        while count<a:
            
            itr = itr.next
            count+=1
            
        left = itr
        
        while count<=b:
            
            itr = itr.next
            count+=1
            
        right = itr
            
        left.next = list2
        

        while list2.next:
            list2 = list2.next
            
        list2.next = right.next
        
        
        return list1
        
        
            
            
                
            
            
            