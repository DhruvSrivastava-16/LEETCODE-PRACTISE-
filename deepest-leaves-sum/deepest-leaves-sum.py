# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    leaf = {}
    
    def leafutil(self,root,h):
        if not root:
            return 
        
        if root.left == None and root.right == None:
            #print(root)
            if h not in self.leaf:
                self.leaf[h] = [root.val]
                #print("updated: ",self.leaf)
            else:
                self.leaf[h].append(root.val)
                #print("updated: ",self.leaf)

            
        
        self.leafutil(root.left,h+1)
        self.leafutil(root.right,h+1)
    
    
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.leaf = {}
        self.leafutil(root,0)
        #print(self.leaf)
        maxh = max(self.leaf.keys())
        ans = 0
        
        
        
        for i in self.leaf[maxh]:
            ans = ans + i
            
        return ans
        