class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        v1 = self.nums
        v2 = vec.nums
        print(v1)
        print(v2)
        ans = 0
        j = 0
        for i in range(0,len(v1)):
            print(v1[i],v2[j])
            ans = ans + v1[i]*v2[j]
            j+=1
            
        return ans
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)