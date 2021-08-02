from collections import deque
from collections import defaultdict

class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        sz = len(nums)
        ans =[]
        dic = defaultdict(lambda: 0)
     
        sz_ans = len(ans)
        
        for i in range(0,k):
            dic[nums[i]]+=1
            dq.append(nums[i])
        
        ans.append(len(set(dq)))
        
        
        for i in range(k,len(nums)):
            
            
            t=dq.popleft()
            dic[t]-=1
            
            dq.append(nums[i])
            
         
            if dic[nums[i]]==0 and dic[t]==0:
                
                dic[nums[i]]+=1
                ans.append(ans[-1])
                
            elif dic[nums[i]]==0 and dic[t]!=0:
                dic[nums[i]]+=1
                ans.append(ans[-1]+1)
                
            elif dic[nums[i]]!=0 and dic[t]==0:
                dic[nums[i]]+=1
                ans.append(ans[-1]-1)
                
            else:
                dic[nums[i]]+=1
                ans.append(ans[-1])
            
           
        
        return(ans)
        