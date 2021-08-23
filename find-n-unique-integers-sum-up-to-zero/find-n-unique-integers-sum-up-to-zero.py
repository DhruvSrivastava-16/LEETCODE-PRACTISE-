class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        
        if n==1:
            return [0]
        
        curr_len = 0
        curr_sum = 0
        
        temp=n
        
        while curr_len!=n:
            
            if n-curr_len == 1:
                ans.append(0)
                curr_len+=1
                
            else:   
                ans.append(-temp)
                ans.append(temp)
                temp -=1
                curr_len +=2
                
        return(ans)
        