class Solution:
    def isPalindrome(self,s,left,right,count):
        
        while left<right:
            
            if s[left]!=s[right]:
            
                if count==1:
                    return False
                
                else:
                    return self.isPalindrome(s,left+1,right,count+1) or self.isPalindrome(s,left,right-1,count+1)
                
            left+=1
            right-=1
            
        return True
            
    
    def validPalindrome(self, s: str) -> bool:
        count = 0
        return self.isPalindrome(s,0,len(s)-1,count)
            
                
            
        
            
        
            
                