class Solution:
    def countSubstrings(self, s: str) -> int:
        
        dp = [[False for i in range(len(s)+1)] for j in range(len(s)+1)]
        ans = 0
        
        for i in range(len(s)):
            dp[i][i] = True
            
        for i in range(len(s)-1):
            dp[i][i+1] = s[i]==s[i+1]

            
        for length in range(3,len(s)+1):
            st = 0
            end = length+st-1
            while end<len(s):
                dp[st][end] = dp[st+1][end-1] and (s[st]==s[end])

                end+=1
                st+=1
        
        for i in range(len(s)):
            for j in range(len(s)):
                if dp[i][j]:
                    ans+=1
                    
        return ans
                
                