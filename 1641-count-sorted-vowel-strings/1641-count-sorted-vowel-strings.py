class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        aCount = [1]*n
        eCount = [1]*n
        iCount = [1]*n
        oCount = [1]*n
        uCount = [1]*n
        
        for i in range(1,n):
            
            aCount[i] = aCount[i-1] + eCount[i-1] + iCount[i-1] + oCount[i-1] + uCount[i-1] 
            eCount[i] = eCount[i-1] + iCount[i-1] + oCount[i-1] + uCount[i-1]
            iCount[i] = iCount[i-1] + oCount[i-1] + uCount[i-1]
            oCount[i] = oCount[i-1] + uCount[i-1]
            
        print(aCount,eCount,iCount,oCount,uCount)
            
        result = aCount[-1] + eCount[-1] + iCount[-1] + oCount[-1] + uCount[-1] 
        
        return result