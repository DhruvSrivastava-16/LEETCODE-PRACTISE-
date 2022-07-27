class Solution:
    
    def helper(self,nums,temp,store,sz,pos):
        if sz==0:
            store.append(temp[:])
            return 
        
        for i in range(pos,len(nums)):
            temp.append(nums[i])
            self.helper(nums,temp,store,sz-1,i+1)
            temp.pop()
        
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        temp = []
        store = []
        
        for sz in range(0,len(nums)+1):
            self.helper(nums,temp,store,sz,0)
            
        return (store)