class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        n1=len(num1)-1
        n2=len(num2)-1
        answer = []
        temp_sum = 0
        carry = 0
        
        while n1>=0 or n2>=0:
            print(temp_sum)
            if n1>=0:
                
                x1=int(num1[n1])
                
            else:
                x1 = 0
                
            if n2>=0:
                x2=int(num2[n2])
                
            else:
                x2 = 0
                
            temp_sum = (x1+x2 + carry)%10
            carry = (x1+x2+carry)//10
            answer.append(str((temp_sum)))
            n1-=1
            n2-=1
        
        print(answer)
        
    
        if carry>0:
            answer.append(str(carry))
            
        print(answer)
        return(''.join(answer[::-1]))
            