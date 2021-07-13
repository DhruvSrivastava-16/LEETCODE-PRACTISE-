class Solution:
    def reverseString(self, s: List[str]) -> None:
        st = 0
        end = len(s) - 1
        
        while st<=end:
            s[st],s[end] = s[end],s[st] 
            st+=1 
            end-=1
            
        """
        Do not return anything, modify s in-place instead.
        """
        