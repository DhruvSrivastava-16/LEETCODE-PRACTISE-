# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def helperSerialize(self,root,st):
        if not root:
            st+='None,'
            return st
        else:
            st+=str(root.val)+','
            st = self.helperSerialize(root.left,st)
            st = self.helperSerialize(root.right,st)
            return st
        
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        st = ''
        st = self.helperSerialize(root,st)
        print(st)
        return st
    
    def helperDeserialize(self,values,root):
        if values[0] == 'None':
            values.pop(0)
            return None
        
        root = TreeNode(values[0])
        values.pop(0)
        root.left = self.helperDeserialize(values,root)
        root.right = self.helperDeserialize(values,root)
        return root
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        values = data.split(',')[:-1]
        print(values)
        root = TreeNode()
        return self.helperDeserialize(values,root)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))