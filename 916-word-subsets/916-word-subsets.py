class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        
        maxFreqMap = defaultdict(int)
        
        for word in words2:
            
            temp = Counter(word)
            
            for k,v in temp.items():
                
                if maxFreqMap[k]<v:
                    maxFreqMap[k] = v
                    
                    
        finalMatcher = ''
        answer = []
        for key, value in maxFreqMap.items():
            
            finalMatcher += key*value
            
        for word in words1:
            
            temp = Counter(word)
            Flag = False
            for k,v in maxFreqMap.items():
                if maxFreqMap[k]>temp[k]:
                    print(maxFreqMap,temp,k)
                    Flag = True
                    break
                    
            if Flag==False:
                answer.append(word)
                
        return answer