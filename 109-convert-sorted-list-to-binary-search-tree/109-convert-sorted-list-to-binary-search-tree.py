# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursion(self,listt):
        if not listt:
            return None
        
        mid = len(listt)//2
        newNode = ListNode(listt[mid])
        
        newNode.left = self.recursion(listt[:mid])
        newNode.right = self.recursion(listt[mid+1:])
        
        return newNode
    
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        listt = []
        
        while head:
            
            listt.append(head.val)
            head = head.next
            
        return self.recursion(listt)