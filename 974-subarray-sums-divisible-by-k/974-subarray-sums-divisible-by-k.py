class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hmap = {0:1}
        prefixSum = 0
        answer = 0
        
        for num in nums:
            
            prefixSum+=num
            rem = prefixSum%k
            
            if rem<0:
                rem = rem+k
                
                
            if rem in hmap:
                answer+=hmap[rem]
                hmap[rem]+=1
                
            else:
                hmap[rem] = 1
                
                
        return answer
                
        