class Solution:
    def str2tree(self, s: str) -> TreeNode:
        return self._str2treeInternal(s, 0)[0]
    
    def _getNumber(self, s: str, index: int) -> (int, int):
        
        is_negative = False
        
        # A negative number
        if s[index] == '-':
            is_negative = True
            index = index + 1
        
        number = 0
        while index < len(s) and s[index].isdigit():
            number = number * 10 + int(s[index])
            index += 1
        
        return number if not is_negative else -number, index
            
    
    def _str2treeInternal(self, s: str, index: int) -> (TreeNode, int):
        
        if index == len(s):
            return None, index
        
        # Start of the tree will always contain a number representing
        # the root of the tree. So we calculate that first.
        value, index = self._getNumber(s, index)
        node = TreeNode(value)
        
        # Next, if there is any data left, we check for the first subtree
        # which according to the problem statement will always be the left child.
        if index < len(s) and s[index] == '(':
            node.left, index = self._str2treeInternal(s, index + 1)
        
        # Indicates a right child
        if index < len(s) and s[index] == '(':
            node.right, index = self._str2treeInternal(s, index + 1)
        
        return node, index + 1 if index < len(s) and s[index] == ')' else index