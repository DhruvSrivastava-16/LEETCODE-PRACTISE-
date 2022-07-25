class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        if len(Counter(s).keys()) > len(Counter(''.join(wordDict)).keys()):
            return []
        
        wordSet = set(wordDict)                  
                                        
        dp = [[]]*(len(s)+1)
        dp[0] = [""]
                                        
        for end in range(1,len(s)+1):
            subList = []
            for start in range(0,end):
                word = s[start:end]
                if word in wordSet:
                    for sub in dp[start]:
                        subList.append((sub+' '+word).strip())
                        
            dp[end] = subList
        
        print(dp)
        return dp[-1]