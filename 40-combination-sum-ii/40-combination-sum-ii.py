class Solution:
    
    def backtrack(self,temp,answer,total,target,pos,nums,counter):
        
        if total==target:
            answer.append(temp[:])
            return 
        
        if total>target:
            return
 
        for i in range(pos,len(counter)):
            ele, freq = counter[i]
            
            if freq<=0:
                continue
        
            total+=ele
            temp.append(ele)
            counter[i] = (ele,freq-1)
            self.backtrack(temp,answer,total,target,i,nums,counter)
            counter[i] = (ele,freq)
            temp.pop()
            total-=ele

    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        temp = []
        answer = []
        total = 0
        pos = 0
        freqMap = Counter(candidates)
        counter = [(c,freqMap[c]) for c in freqMap.keys()]
        self.backtrack(temp,answer,total,target,pos,candidates,counter)
    
        
        return(answer)
        