from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        a={}
        for i in arr:
            if i not in a:
                a[i] = 1
                
            else:
                a[i] = a[i] + 1
                
        
        print(a)
        b = []
        for i in a.keys():
            b.append([i,a[i]])
        print(b)
        b.sort(key = lambda a:a[1])
        
        for i in b:
            if k==0:
                break 
                
            if i[1]>=k:
                i[1] = i[1]-k
                k = 0
            
            else:
                k = k-i[1]
                i[1]=0
        
        ans = 0
        
        for i in b:
            if i[1] == 0:
                continue
            
            else:
                ans +=1
        return(ans)
