class Solution:
    
    
    def isValid(self,segment):
        # print('SEG:',segment,segment[0],segment[0]=='0')
        if len(segment)>1 and segment[0]=='0'  :

            return False
        
        if segment and int(segment)>255:
            return False
        
        return True
    
    def append(self,segments,answer):
        
        answer.append('.'.join(segments))
        
    def backtrack(self,answer,dots,segments,pos,s):
        if dots == 0 and pos == len(s):
            self.append(segments,answer)
            
        # return
            
        for cP in range(pos,len(s)):
            segment = s[pos:cP+1]
            if self.isValid(segment):
                segments.append(segment)
                self.backtrack(answer,dots-1,segments,cP+1,s)
                segments.pop()
            
    
    def restoreIpAddresses(self, s: str) -> List[str]:
        answer = []
        dots = 4
        segments = []
        pos = 0
        self.backtrack(answer,dots,segments,pos,s)
            
            
        return(answer)