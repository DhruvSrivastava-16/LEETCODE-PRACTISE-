class Solution:
    def gen_sub_len(self,nums,l,pos,temp):
        if len(temp)==l:
            self.ans.append(temp[:])
            return 
            
        for i in range(pos,len(nums)):
            temp.append(nums[i])
            self.gen_sub_len(nums,l,i+1,temp)
            temp.pop()
    
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        
        for l in range(0,len(nums)+1):
            temp = []
            self.gen_sub_len(nums,l,0,temp)

            
        return self.ans
    
    
