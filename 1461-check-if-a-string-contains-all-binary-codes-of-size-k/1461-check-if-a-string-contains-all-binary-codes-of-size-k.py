class Solution:
    def genSub(self,k,store,temp,zs,os):
        if len(temp)==k:
        
            store.append(''.join(temp))
            return 
        
        if zs<k:
            temp.append('0')
            self.genSub(k,store,temp,zs+1,os)
            temp.pop()
            
        if os<k:
            temp.append('1')
            self.genSub(k,store,temp,zs,os+1)
            temp.pop()
            
    def hasAllCodes(self, s: str, k: int) -> bool:
#         store = []
#         temp = []
#         self.genSub(k,store,temp,0,0)
#         for itr in store:
#             if itr not in s:
#                 return False
            
#         return True

        need = 1<<k
        found = set()
        
        for i in range(k,len(s)+1):
            temp = s[i-k:i]
            if temp not in found:
                found.add(temp)
                need-=1
                
            if need == 0:
                return True
        return False