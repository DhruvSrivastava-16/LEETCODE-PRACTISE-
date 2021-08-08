# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        l = []
        
        for i in lists:
            temp = i
            while temp:
                l.append(temp.val)
           
                temp = temp.next

        
        Head = ListNode()
        Temp = ListNode()
        Head = Temp
        
        heapq.heapify(l)
        while l:
            
            j = heapq.heappop(l)
            Temp.next = ListNode(j)
            Temp = Temp.next
            
            
        return Head.next
        