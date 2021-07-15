class Solution:
    def tranform_steps(self,s,t,dic_s,dic_t):
        ans = 0
        done = []
        for i in dic_s.keys():
            if i not in dic_t:
                ans = ans + dic_s[i]
            
            elif dic_s[i]>dic_t[i]:
                ans = ans + (dic_s[i]-dic_t[i])
            
                
        return ans
                
        
         
    def minSteps(self, s: str, t: str) -> int:
        dic_s = {}
        dic_t = {}
        
        for i in s:
          
            if i not in dic_s:
                dic_s[i] = 1
            else:
                dic_s[i] +=1
            
         
        for i in t:
            if i not in dic_t:
                dic_t[i] =1 
            
            else:
                dic_t[i] +=1
                
        ans = self.tranform_steps(s,t,dic_s,dic_t)
        
        return ans
                
        
            
        