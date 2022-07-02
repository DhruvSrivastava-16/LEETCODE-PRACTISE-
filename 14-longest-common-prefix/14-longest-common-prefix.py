class Solution:
    def lcp(self,string1,string2):
        itr1, itr2 = 0, 0
        common = ''
        
        while itr1<len(string1) and itr2<len(string2):
            if string1[itr1]==string2[itr2]:
                common+=string1[itr1]
                
            else:
                return common
            
            itr1+=1
            itr2+=1
        
        return common
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs)==1:
            return strs[0]
        
        cp = self.lcp(strs[0],strs[1])
        
        if len(strs)==2:
            return cp
        
        for i in range(2,len(strs)):
            cp = self.lcp(cp,strs[i])
            
        return cp