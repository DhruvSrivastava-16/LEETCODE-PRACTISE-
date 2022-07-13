# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def levels(self,root,level,store):
        if not root:
            return 
        
        store[level].append(root.val)
        self.levels(root.left,level+1,store)
        self.levels(root.right,level+1,store)
        
    
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        store = defaultdict(list)
        self.levels(root,0,store)
        answer = []
        
        for k, v in store.items():
            if k%2!=0:
                answer.append(v[::-1])
            else:
                answer.append(v)
                
        return answer