class Solution:
    def isPali(self,word):
        rev = word[::-1]
        
        if word==rev:
            return True
        
        return False
    
    def dfs(self,word,pos,answer,temp):
        if pos==len(word):
            answer.append(temp[:])
            return
        
        for itr in range(pos+1,len(word)+1):
            if self.isPali(word[pos:itr]):
                temp.append(word[pos:itr])
                self.dfs(word,itr,answer,temp)
                temp.pop()
                
                
            
    
    def partition(self, s: str) -> List[List[str]]:
        
        
        answer = []
        temp = []
        self.dfs(s,0,answer,temp)
        return answer