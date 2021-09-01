from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        t = Counter(nums)
        print(t)
        print(t.values())
        for i in t.values():
        
            if i>=2:
            
                return True
        
        return False