# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        
        self.index = -1
        self.arr = []
        self._inorder(root)
        
    def _inorder(self,root):
        if root is None:
            return 
        
        self._inorder(root.left)
        self.arr.append(root.val)
        self._inorder(root.right)
        
        

    def next(self) -> int:
        self.index+=1
        return self.arr[self.index]        

    def hasNext(self) -> bool:
        return self.index+1<len(self.arr)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()