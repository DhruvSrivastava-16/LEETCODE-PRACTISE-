class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        seen = dict()
        l = 0
        r = 0
        ans = 0
        count = 0
        itr = 0
        
        while r<len(s):
            if s[r] in seen and seen[s[r]]>=l:
                l = max(seen[s[r]],-5)+1
            
            ans = max(ans,r-l+1)
            seen[s[r]] = r
            r+=1
        
        return ans 
            
            
            