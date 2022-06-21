class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l, r, ans = 0, 0 ,0
        seen = dict()
        
        while r<len(s):
            
            if s[r] in seen:
                l = max(seen[s[r]],l) 
            
            ans = max(ans,r-l+1)
            print(r,l,ans)
            seen[s[r]] = r + 1
            r+=1
        
        return ans