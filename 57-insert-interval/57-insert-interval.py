class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        
        intervals.append(newInterval)
        intervals.sort(key = lambda x:(x[0],x[1]))
        print(intervals)
        i=0
        while i<len(intervals)-1:
            
            while i<len(intervals)-1 and intervals[i+1][0]>=intervals[i][0] and intervals[i+1][0]<=intervals[i][1]:
                if intervals[i+1][1]>intervals[i][1]:
                    intervals[i][0] = min(intervals[i+1][0],intervals[i][0])
                    intervals[i][1] = max(intervals[i+1][1],intervals[i][1])
                    intervals.pop(i+1)
                
                else:
                    intervals.pop(i+1)
                
            i+=1
                
        return intervals
                