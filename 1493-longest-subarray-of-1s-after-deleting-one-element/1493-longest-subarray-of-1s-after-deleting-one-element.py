class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        L = 0
        R = 0
        ans = 0
        count_of_zeros = 0
        #start the sliding window process!
        while R < len(nums):
            if(nums[R] == 0):
                count_of_zeros += 1
            #stopping condition!
            while count_of_zeros == 2:
                ans = max(ans, R - L - 1)
                #potentially before contracting window, check if left is pointing to a zero!
                if(nums[L] == 0):
                    count_of_zeros -= 1
                L += 1
            #continue expanding sliding window!
            R += 1
        
        #edge case: if count_of_zeros of input array is ever less than or equal to 1, then
        #recompute it!
        if(count_of_zeros <= 1):
            ans = max(ans, R - L - 1)
        return ans