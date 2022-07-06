class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        
        l = 0
        r = 0
        ans = -float('inf')
        seen = dict()
        
        while r<len(s):
            
            if s[r] in seen:
                l = max(seen[s[r]]+1,l)
                
            ans = max(ans,r-l+1)
            seen[s[r]]=r
            r+=1
            
        return ans
                
            