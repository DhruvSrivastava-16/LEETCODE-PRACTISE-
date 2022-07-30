class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda x:len(x),reverse = True)
        dp = {word:1 for word in words}
        
        
        for itr in range(len(words)-1,-1,-1):
            temp = 1
            for i in range(0,len(words[itr])):
                tempW = words[itr][:i]+words[itr][i+1:]
                word = words[itr]
                if word in dp and tempW in dp:
                    dp[word] = max(dp[word],1+dp[tempW])
                
        return max(list([v for k,v in dp.items()]))
                