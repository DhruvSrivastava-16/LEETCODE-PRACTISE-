class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # quick check on the characters,
        #   otherwise it would exceed the time limit for certain test cases.
        if set(Counter(s).keys()) > set(Counter("".join(wordDict)).keys()):
            return []
        
        wordSet = set(wordDict)
        
        dp = [[]]*(len(s)+1)
        dp[0] = [""]
        
        for end in range(1,len(s)+1):
            
            sub = []
            
            for st in range(0,end):
                
                word = s[st:end]
                
                if word in wordSet:
                    
                    for sq in dp[st]:
                        
                        sub.append((sq+' '+word).strip())
                        
            dp[end] = sub
            print(dp,sub)
        return dp[-1]