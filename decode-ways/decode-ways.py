class Solution:
    def numDecodings(self, s: str) -> int:
        DP = [0]*(len(s)+1)
        DP[0] = 1
        if s[0]=='0':
            DP[1] = 0
        
        else:
            DP[1] = 1
            
        for i in range(2,len(DP)):
            if s[i-1]!='0':
                DP[i] = DP[i-1]
                
            two_d = int(s[i-2:i])
            if two_d >=10 and two_d<=26:
                DP[i] += DP[i-2]
                
        return DP[len(s)]