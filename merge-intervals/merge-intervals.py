class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        merged = []
        intervals.sort(key = lambda x:x[0])
        
        for interval in intervals:
            print(merged)
            if merged:
                print('y')
                if merged[-1][0]<=interval[0] and merged[-1][1]>=interval[0]:
                    merged[-1][1] = interval[1] if interval[1]> merged[-1][1] else merged[-1][1]
                
                else:
                    merged.append(interval)
                
            else:
                print('em')
                merged.append(interval)
                
        return merged