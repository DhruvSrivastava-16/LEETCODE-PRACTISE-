# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        bigger_pq = p if p.val>q.val else q
        smaller_pq =  p if p.val<q.val else q
        print("B: ",bigger_pq.val)
        print("S: ",smaller_pq.val)
        print("R: ",root.val)
        
     
        
        if smaller_pq.val>root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        
        elif bigger_pq.val<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
            
        else:
            return root
        
        
                
        
        
        
        
        
        
            