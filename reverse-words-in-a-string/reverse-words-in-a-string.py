class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.split(' ')
        print(words)
        words = words[::-1]
        print(words)
        
        ans = ''
        
        for i in range(0,len(words)):
            if words[i] == '':
                continue
                
            ans += words[i] + ' '
            
        return(ans[:-1])
        