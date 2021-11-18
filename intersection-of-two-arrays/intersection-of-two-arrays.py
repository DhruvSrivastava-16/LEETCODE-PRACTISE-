class Solution(object):
    def intersection(self, nums1, nums2):
        C = [i for i in nums1 if i in nums2]
        return set(C)
        