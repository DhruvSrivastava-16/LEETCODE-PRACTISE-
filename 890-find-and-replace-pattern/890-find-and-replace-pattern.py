class Solution:
    def generatePattern(self,string):
        hmap = defaultdict(int)
        ctr = 1
        code = '.'
        
        for itr in string:
            if itr not in hmap:
                hmap[itr] = ctr
                code+=str(ctr)+'.'
                ctr+=1
                
            else:
                code+=str(hmap[itr])
                
        return code
        
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        
        find = self.generatePattern(pattern)
        
        answer = []
        
        for word in words:
            
            tempPattern = self.generatePattern(word)
            print(tempPattern,find)
            if tempPattern == find:
                
                answer.append(word)
                
        return answer