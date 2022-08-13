class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefixProd = 1
        countZero = 0
        
        for itr in range(len(nums)):
            
            if nums[itr]!=0:
                prefixProd*=nums[itr]
                
            else:
                countZero +=1 
                
        if countZero > 1:
            return [0 for itr in range(len(nums))]

        
        
        answer = []
        
        for itr in range(len(nums)):
            if nums[itr]!=0:
                if countZero!=0:
                    answer.append(0)
                    
                else:
                    answer.append(prefixProd//nums[itr])
                
            else:
                if countZero!=1:
                    print('CZ:',countZero)
                    answer.append(0)
                    
                else:
                    answer.append(prefixProd)
                
                
        return answer