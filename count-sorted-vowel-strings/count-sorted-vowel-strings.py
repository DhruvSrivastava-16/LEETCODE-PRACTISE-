class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = ['a','e','i','o','u']
        ans = {0:[],1:['a','e','i','o','u']}
        
        for i in range(2,n+1):
            temp = []
            for j in range(0,5) :
                prev = ans[i-1]
                tc = ""
                for k in prev:
                    if vowels[j]<=k[0]:
                        tc = vowels[j]+k
                        temp.append(tc)
                
                #prev = prev[():]
            ans[i] = temp
        return len(ans[n])
        
                    
                     
                
                
                
        