class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr)==1:
            return True
        
        if len(arr)==2:
            return True
        
        arr.sort(reverse=True)
        c = arr[1]-arr[0]
        f=0
        for i in range(0,len(arr)-1):
            if arr[i+1]-arr[i]!=c:
                f=-1
                break;
        
        arr.sort()
        c = arr[1]-arr[0]
        k = 0
        for i in range(0,len(arr)-1):
            if arr[i+1]-arr[i]!=c:
                k=-1
                break;
                
        if k==-1 and f==-1:
            return False
        
        return True

        