class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        merged = []
        
        for interval in intervals:
            
            if len(merged)==0:
                merged.append(interval)
                continue
                
            if merged[-1][0]<=interval[0] and merged[-1][1]>=interval[0]:
                merged[-1][1] = interval[1] if interval[1]> merged[-1][1] else merged[-1][1]
            
            else:
                merged.append(interval)
                
            #return(merged)
                
        return(merged)
        
                
            
        