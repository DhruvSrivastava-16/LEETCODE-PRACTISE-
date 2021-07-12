class Solution:
    cache = {}
    
    def help(self,val):
        
        if val not in self.cache:
                self.cache[val] = 0
        
        print("Val: ",val)
        if val <= 1:
            
            return 0
        
        if val%2==0:
            
            self.cache[val] = self.help(val//2)+1
            return self.cache[val]
        else:
            self.cache[val] = self.help(val*3+1)+1
            return self.cache[val]
        
        
        
        
        
    def getKth(self, lo: int, hi: int, k: int) -> int:
       
        for j in range(2,hi+1):
            print(j)
            if j not in self.cache:
                self.cache[j] = 0
            
            if self.cache[j]==0:
                self.help(j)
        
        #print(self.cache.items())
        #k = list(self.cache.items())
        #k.sort()
        #print(k)
        ans = []
        for j in range(lo,hi+1):
            ans.append([j,self.cache[j]])
        
        ans.sort(key= lambda x:x[1])
        print(ans)
        return ans[k-1][0]
            
            
        
        