class Solution:
    def maximum69Number (self, num: int) -> int:
        s_num = str(num)
        ans = ''
        f =0
        for i in range(0,len(s_num)):
            print(s_num[i])
            if s_num[i] == '6':
                ans = s_num[:i] + '9' + s_num[i+1:]
                f = -1
                break
        
        if f == 0:
            return num
                
        return (int(ans))
        