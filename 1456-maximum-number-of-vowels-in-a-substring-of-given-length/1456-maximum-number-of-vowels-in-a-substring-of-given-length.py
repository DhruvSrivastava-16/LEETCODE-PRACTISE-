class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        left = 0
        right = 0
        vowels = "aeiou"
        tempCount = 0
        answer = -float('inf')
        
        while right<len(s) and left<=right:
            
            while right-left+1<=k:
                
                if s[right] in vowels:
                    
                    tempCount+=1
                    
                right+=1
                
            answer = max(answer,tempCount)
            
            while right-left+1>k:
                
                if s[left] in vowels: 
                    tempCount-=1
                    
                left+=1
                
        return answer
                    
                
                