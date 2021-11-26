class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        if len(arr)==1:
            return 1
        
        maxx = arr[0]
        count = 0
        
        for i in range(0,len(arr)):
            
            if arr[i]>maxx:
                maxx = arr[i]
                
            if maxx == i:
                count+=1
                
        return count
            