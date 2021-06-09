class Solution:
    def isValid(self, s) -> bool:
        stack = []
        bra = {'{':'}','(':')','[':']'};
       
        
        if len(s)%2!=0:
            return False
        
        for i in s:
            sz = len(stack)
            print(i)
            if i in bra:
                stack.append(i)
                
            else:
                if sz!=0:
                    temp = stack.pop()
                    if(bra[temp]!=i):
                        return False
                    
                else:
                    return False
        if(len(stack)!=0):
            return False
                
        return True