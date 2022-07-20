class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        counter = defaultdict(int)
        maximum = 0
        
        for index in range(len(s)):
            counter[s[index]] +=  1
            
            while (index-left + 1) - max(counter.values()) > k:
                counter[s[left]] -= 1
                left += 1
                
            maximum = max(maximum, index-left+1)
            
        return maximum