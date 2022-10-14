class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if set(Counter(s).keys()) > set(Counter("".join(wordDict)).keys()):
            return []
        
        wordSet = set(wordDict)
        
        dp = [[]]*(len(s)+1)
        # print(dp)
        
        dp[0] = " "
        
        for end in range(1,len(s)+1):
            
            temp = []
            
            for st in range(0,end):
                
                wrd = s[st:end]
                
                if wrd in wordSet:
                    
                    for sq in dp[st]:
                    
                        temp.append((sq+" "+wrd).strip())
                    
            dp[end] = temp
            
        return dp[-1]
                
            