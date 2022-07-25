class Solution:
    def countSubstrings(self, s: str) -> int:
        
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        ans = 0
        
        for i in range(0,len(s)):
            dp[i][i] = True
            
        for i in range(0,len(s)-1):
            dp[i][i+1] = s[i] == s[i+1]
            
        for length in range(3,len(s)+1):
            st = 0
            end = st+length-1
            
            while end<len(s):
                dp[st][end] = dp[st+1][end-1] and s[st]==s[end]
                st+=1
                end+=1
                
        for i in range(len(s)):
            for j in range(len(s)):
                if dp[i][j]:
                    ans+=1
                    
        return ans