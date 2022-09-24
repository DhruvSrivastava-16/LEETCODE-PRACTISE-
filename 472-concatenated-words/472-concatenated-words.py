class Solution:
    
    def dfs(self,loc,word,count, wordSet):
        if loc>=len(word):
            if count>1:
                return True
            
            else:
                return False
            
        for idx in range(loc,len(word)):
            
            if word[loc:idx+1] in wordSet and self.dfs(idx+1,word,count+1,wordSet):
                return True

        return False
            
        
    
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = set(words)
        answer = []

        for i in range(len(words)):
            count = 0
            if self.dfs(0,words[i],count,wordSet):
                answer.append(words[i])
                
        return(answer)