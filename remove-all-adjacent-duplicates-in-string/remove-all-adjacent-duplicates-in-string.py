class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans = s[0]
        for i in range(1,len(s)):
            #print(s,ans)
            if len(ans)>0 and s[i]==ans[-1]:
                ans = ans[:-1]
                continue
            
            ans = ans + s[i]
                
        return(ans)
        