class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        k = []
        
        for i in nums:
            k.append(i)
            
        k.sort() 
      
        
        hm = {}
        for i in range(0,len(k)):
            
            if k[i] not in hm:
                hm[k[i]] = i
                
        ans = []
        
        for j in nums:
            ans.append(hm[j])
        
        return (ans)
            
        
            
            
            