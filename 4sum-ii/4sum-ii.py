class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        dic = {}
        
        for a in nums1:
            for b in nums2:
                if (a+b) not in dic:
                    dic[a+b] = 1
                    
                else:
                    dic[a+b] +=1
                    
        cnt = 0
                    
        for c in nums3:
            for d in nums4:
                if -(c+d) in dic:
                    cnt += dic[-(c+d)]
                
        return cnt