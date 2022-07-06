# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        
        seen = set()
        delete = set()
        temp = head
        prev = None
            
        while temp:
            if temp.val not in seen:
                seen.add(temp.val)
                prev = temp
                temp = temp.next
                continue
                
            else:
                delete.add(temp.val)
                prev.next = temp.next
                temp = temp.next 
        
        temp = head
        prev = None
        
        while temp:
            
            if temp.val in delete:
                if prev:
                    prev.next = temp.next
                    temp = temp.next
                    continue
                    
                else:
                    itr = temp
                    head = temp.next
                    temp = temp.next
                    prev = None
                    continue
                    
            prev = temp
            temp = temp.next
                    
                    
        return head
            
            
                
                
    
        
                
        
            
            
            
            
                
                
                