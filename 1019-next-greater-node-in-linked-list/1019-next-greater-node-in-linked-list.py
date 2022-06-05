# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import defaultdict

class Solution:
    def popping(self, stk, val, idx,ans):
        
        while stk and stk[-1][0]<val:
            
            value, loc = stk.pop()
            ans[loc] = val
            
            
    
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        
        stk = []
        ans = defaultdict(int)
        idx = 0
        nodes = 0
        
        
        
        while head:
            if stk:
                
                if head.val > stk[-1][0]:
                    self.popping(stk, head.val, idx, ans)
                
            

            stk.append([head.val, idx])
                
                
            head = head.next
            nodes+=1
            idx+=1
            
        final = []    
        for i in range(idx):
            if i in ans:
                final.append(ans[i])
            else:
                final.append(0)
                
        return final
