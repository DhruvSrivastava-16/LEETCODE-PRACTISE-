class Solution:
    def generate_subset_len(self,l,temp,nums,pos):
        if len(temp) == l:
            self.ans.append(temp[:])
            return
        
        for i in range(pos,len(nums)):
            temp.append(nums[i])
            self.generate_subset_len(l,temp,nums,i+1)
            temp.pop()
        
        
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        for i in range(0,len(nums)+1):
            
            self.generate_subset_len(i,[],nums,0)
            
        return(self.ans)