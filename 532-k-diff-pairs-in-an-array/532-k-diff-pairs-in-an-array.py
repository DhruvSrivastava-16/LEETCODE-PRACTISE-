from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        numSet = set(nums)
        ansSet = set()
        
        if k==0:
            fmap = Counter(nums)
            return len([k for k in fmap.values() if k>1])
    
        else:
            for num in nums:
                if k+num in numSet:
                    ansSet.add((num,k+num))
                

        # print(numSet)
        return len(ansSet)