class Solution:
    def lcp(self,s1,s2):
        ans = ""
        
        for i in range(0,min(len(s1),len(s2))):
            if s1[i] == s2[i]:
                ans+=s1[i]
            
            else:
                break
                
        return ans
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        
        if len(strs)==2:
            return self.lcp(strs[0],strs[1])
        
        local = self.lcp(strs[0],strs[1])
        
        for i in range(2,len(strs)):
            local =  self.lcp(local,strs[i])
            if local=="":
                return local
            
        return local