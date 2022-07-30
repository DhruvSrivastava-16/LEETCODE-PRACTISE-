class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        
        slots = 1
        listt = preorder.split(',')
        
        for n in listt:
            
            slots-=1
            
                            
            if slots<0:
                return False
            
            if n!='#':
                slots += 2

                
        return slots==0