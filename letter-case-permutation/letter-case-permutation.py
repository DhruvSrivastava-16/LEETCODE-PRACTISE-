class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = [[]]
        n = len(s)
        
        for char in s:
            n = len(ans)
            if char.isalpha():
                for i in range(n):
                    ans.append(ans[i][:])
                    ans[i].append(char.lower())
                    ans[i+n].append(char.upper())
                    
                    
            else:
                for i in range(n):
                    ans[i].append(char)
                        
                        
        return map("".join, ans)
                
            
        