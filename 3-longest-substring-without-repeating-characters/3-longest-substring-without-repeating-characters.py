class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        seen = dict()
        l = 0
        r = 0
        ans = 1
        count = 0
        itr = 0
        
        while r<len(s):
            if s[r] in seen:
                l = max(seen[s[r]],l)
            
            ans = max(ans,r-l+1)
            seen[s[r]] = r+1
            r+=1
        
        print(seen)    
        return ans 
            
            
            