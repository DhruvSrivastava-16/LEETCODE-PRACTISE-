class Solution:
    def dfs(self,s,partition,ans):
        if len(s)==0:
            ans.append(partition[:])
            
        for i in range(1,len(s)+1):
            pre = s[:i]
            post = s[i:]
            
            if self.pal(pre):
                partition.append(pre)
                self.dfs(post,partition,ans)
                partition.pop()
                
    def pal(self,s):
        rev = s[::-1]
            
        return rev==s
    
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.dfs(s,[],ans)
        return(ans)