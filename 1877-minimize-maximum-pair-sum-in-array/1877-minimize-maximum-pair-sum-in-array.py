import heapq

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        leftPtr = 0
        rightPtr = len(nums)-1
        
        pairs = []
        same = []
        
        while leftPtr<rightPtr:

            pairs.append(nums[leftPtr]+nums[rightPtr])
            leftPtr+=1
            rightPtr-=1
            
        return max(pairs)
                
                
                
                
            
            