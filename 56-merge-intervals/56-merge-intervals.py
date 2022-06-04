class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x:x[0])
        
        merge = []
        
        for itr in intervals:
            
            if not merge:
                
                merge.append(itr)
                
            else:
                
                if itr[0]<=merge[-1][1]:
                    
                    merge[-1][1] = max(itr[1],merge[-1][1])
                    
                else:
                    
                    merge.append(itr)
                    
        return merge
                    
                    