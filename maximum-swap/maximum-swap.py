class Solution:
    def getindex(self,x):
        maxx = '0'
        idx = -1
        for i in range(0,len(x)):
            if x[i]>=maxx:
                idx = i
                maxx = x[i]
                
        return idx
            
    def maximumSwap(self, num: int) -> int:
        str_num = list(str(num))
        
        for i in range(0,len( str_num)-1):
            
                
            if str_num[i]<max(str_num[i+1:]):
                idx = self.getindex(str_num[i+1:])
                idx = (idx + i+1)
                str_num[i],str_num[idx]  = str_num[idx],str_num[i]
                print(str_num)
                break
                
        ans = "".join(str_num)
        ans = int(ans)
        return(ans)
        