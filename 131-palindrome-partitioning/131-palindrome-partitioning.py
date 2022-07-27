class Solution:

    def isPali(self,s):
        return s==s[::-1]
    
    def partition(self, s: str) -> List[List[str]]:
        
        store = []
        part = []
        
        def dfs(i):
            if i>=len(s):
                store.append(part[:])
                return
                
            for j in range(i,len(s)):
                if self.isPali(s[i:j+1]):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
                
        dfs(0)
        return (store)