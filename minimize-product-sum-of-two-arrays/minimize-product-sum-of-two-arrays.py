class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        summ=0
        j =0 
        for i in range(0,len(nums1)):
            summ = summ + nums1[i]*nums2[len(nums1)-i-1]
          
                
        return summ
