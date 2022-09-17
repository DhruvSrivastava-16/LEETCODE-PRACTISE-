class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        
        for crtc in s:
            
            if crtc==']':
                print('in:',stk)
                temp = ''
                while stk and stk[-1]!='[':
                    temp=stk.pop()+temp
                # temp = temp
                    
                stk.pop()
                print(stk,temp)
                num = ''
                while stk and stk[-1].isdigit():
                    
                    num  = stk.pop()+num
                    print('N:',num.isdigit())
                temp = int(num)*temp
                # stk.pop()
                print('temp:',temp,num)
                stk.append(temp)
                    
            else:
                stk.append(crtc)
                
        return ''.join(stk)
                
            