import heapq

class Solution:
    
    def genString(self,a,b,c,string,total):
        if len(string) == total:
            return string
        
        
    
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        
        total = a+b+c
        answer = self.genString(a,b,c,'',total)
        string = ''
        heap = [[-a,'a'],[-b,'b'],[-c,'c']]
        heapq.heapify(heap)
        itr=0
        
        while heap:
            letter=''
            val, letter  = heapq.heappop(heap)
            val = -val

            if len(string)>=2 and string[-2:]==letter*2:
                if heap:
                    val2, letter2  = heapq.heappop(heap)
                    val2 = -val2
                    if val!=0:
                        heapq.heappush(heap,[-val,letter])
                    val = val2
                    letter = letter2
                    
                else:
                    return string

            if val != 0:
                string+=letter
                val=val-1
            
            if val>=1:
                heapq.heappush(heap,[-val,letter])

        return string