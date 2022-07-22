class Solution:
    
    
    def convert(self, s: str, numRows: int) -> str:
        
        answer = ''
        itr = 0
        rowMap = defaultdict(list)
        
        while itr<len(s):
            
            row = 0
            rowMap[row].append(s[itr])
        
            temp = numRows-1
            
            itr+=1
            while itr<len(s) and temp>0:
                row+=1
                rowMap[row].append(s[itr])
                temp-=1
                itr+=1

                
            diag = numRows-2
            while itr<len(s) and diag>0:
                row-=1
                rowMap[row].append(s[itr])
                diag-=1
                itr+=1

        
        answer = ''
        
        for value in rowMap.values():
            answer+=''.join(value)
            
        return answer
            
            
            