
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        itr = head
        
        while itr and itr.next:
            
            if itr.val == itr.next.val:
                itr.next = itr.next.next
             
            else:
                itr = itr.next
            
        
        
                
                
        return head        
        
                
                
        