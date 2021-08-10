# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    dic = {}
    def inorder(self,root):
        if not root:
            return 
        
        self.inorder(root.left)
        if root.val not in self.dic:
            self.dic[root.val] = 1
        
        else:
            self.dic[root.val] += 1
        self.inorder(root.right)
        
    
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.dic = {}
        self.inorder(root)
        a = [i for i in self.dic.items()]
     
        print(a)
        a.sort(key = lambda a:a[1],reverse=True)
        maxx=a[0][1]
        ans = []
        for i in a:
            if self.dic[i[0]]==maxx:
                ans.append(i[0])
                
        return(ans)
            
       