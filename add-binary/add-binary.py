class Solution:
    def addBinary(self, a, b) -> str:
        n = max(len(a),len(b))
        a = a.zfill(n)
        b = b.zfill(n)
        c = 0
        answer = []
        
        for i in range(n-1,-1,-1):
            if a[i]=='1':
                c+=1
                
            if b[i]=='1':
                c+=1
                
            answer.append(str(c%2))
            c//=2
            
        print(c)
        if c==1:
            answer.append('1')
            
        answer = answer[::-1]
        answer = ''.join(answer)
        return answer