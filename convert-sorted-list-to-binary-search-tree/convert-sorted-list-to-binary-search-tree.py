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
    def build(self,l):
        if  len(l)<=0:
            return 
        
        mid = len(l)//2
        r = TreeNode(l[mid])
        r.left = self.build(l[:mid])
        r.right = self.build(l[mid+1:])
        return r
        
    
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        l = []
        while head:
            l.append(head.val)
            head = head.next
            
        root=self.build(l)
        return root
        