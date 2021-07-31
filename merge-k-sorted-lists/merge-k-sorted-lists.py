# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        l = []
        heapq.heapify(l)
        for i in lists:
            temp = i
            while temp:
                heapq.heappush(l,temp.val)
           
                temp = temp.next

        
        Head = ListNode()
        Temp = ListNode()
        Head = Temp
        
        
        while l:
            
            j = heapq.heappop(l)
            Temp.next = ListNode(j)
            Temp = Temp.next
            
            
        return Head.next
        