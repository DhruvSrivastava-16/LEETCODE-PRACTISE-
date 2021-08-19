class Solution:
    sub_sets = []
    
    def gen_subsets(self,nums,k,first,temp):
        if len(temp) == k:
            #print("T: ",temp)
            self.sub_sets.append(temp[:])
            #print(self.sub_sets)
            return
            
        for i in range(first,len(nums)):
            #print(k)
            temp.append(nums[i])
            self.gen_subsets(nums,k,i+1,temp)
            #print(self.sub_sets)
            temp.pop()
            
        
    def subsetXORSum(self, nums: List[int]) -> int:
        sz = len(nums)
        self.sub_sets = []
        
        for k in range(0,len(nums)+1):
            
            self.gen_subsets(nums,k,0,[])
            
        result = 0
        temp = 0
        for i in self.sub_sets:
            if len(i)==0:
                continue
            
            temp = 0
            
            for j in i:
                
                temp = temp^j
                
            print(temp)
            result += temp
        
       
        return(result)