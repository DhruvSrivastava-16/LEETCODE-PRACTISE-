
class Solution:
    max_avg = 0
    
    def findavg(self,root):
        if not root:
            return (0,0)
        
        total_sum_l, total_nodes_l = self.findavg(root.left) 
        total_sum_r, total_nodes_r = self.findavg(root.right)
      
        total_sum = total_sum_l + total_sum_r + root.val
        total_nodes = total_nodes_l + total_nodes_r + 1
        
        avg =  total_sum/total_nodes
        
        if self.max_avg<=avg:
            self.max_avg = avg
      
            
        print(total_sum,total_nodes)
        return (total_sum,total_nodes)
    
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        if not root:
            return 0
        
        arr = []
        self.max_avg = 0
        self.findavg(root)
        return(self.max_avg)