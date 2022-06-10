class Solution:
    
    def backtracking(self,ans,temp_str,n,c,o):
        if len(temp_str)==2*n:
            ans.append(temp_str)
            return 
        
        if c<o:
            temp_str+=')'
            c+=1
            self.backtracking(ans,temp_str,n,c,o)
            temp_str=temp_str[:-1]
            c-=1
            
        if o<n:
            temp_str+='('
            o+=1
            self.backtracking(ans,temp_str,n,c,o)
            temp_str=temp_str[:-1]
            o-=1
            
        return 
        
    
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        temp_str = ''
        c, o = 0, 0
        self.backtracking(ans,temp_str,n,c,0)
        return ans
        