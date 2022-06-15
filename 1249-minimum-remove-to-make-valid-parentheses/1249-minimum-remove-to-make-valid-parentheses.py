class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        brackets = []
        for i in range(len(s)):
            
            if s[i]==')':
                
                if not brackets:
                    brackets.append([s[i],i])
                
                elif brackets[-1][0]!='(':
                    brackets.append([s[i],i])
                    
                else:
                    brackets.pop()
                
            elif s[i]=='(': 
                brackets.append([s[i],i])
                
        sett = set()
        
        for i in brackets:
            sett.add(i[1])
            
        ans = ''
        for j in range(0,len(s)):
            if j in sett:
                continue
            
            ans+=s[j]
            
        return ans
            
            
        
        