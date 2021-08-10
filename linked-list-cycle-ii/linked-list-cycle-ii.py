# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = {}
        print(head)
        
        while head:
            if head in visited:
                print("Cycle!")
                return head
                
                
            else:    
                visited[head] =True
                head = head.next
            
        return(None)