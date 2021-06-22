class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:        
        self.results = []
        
        self.helper(root)
        
        return self.results
    
    def helper(self, root):
        if not root:
            return
        
        if not root.left and not root.right:
            return
        
        if not root.left:
            self.results.append(root.right.val)
            self.helper(root.right)

        elif not root.right:
            self.results.append(root.left.val)            
            self.helper(root.left)
        
        else:
            self.helper(root.left)
            self.helper(root.right)