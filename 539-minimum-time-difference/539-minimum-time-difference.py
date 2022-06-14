class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []
        for time in timePoints:
            
            time = time.split(':')
            hr, mins = int(time[0]),int(time[1])

            total = hr*60 + mins
            
            times.append(total)
            
        minn = float('inf')
        times.sort()
        for itr in range(0,len(times)-1):
            if minn >= times[itr+1]-times[itr]:
                minn = times[itr+1]-times[itr]
        print(minn,times)
        return(min(minn,60*24-times[-1]+times[0]))
        
            