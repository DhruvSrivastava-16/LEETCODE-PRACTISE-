from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        di=Counter(nums)
        li=list(di.items())
        
        #keep a list of frequency elements and their values[val,freq]
        
        li.sort(key=lambda x:(x[1],-x[0]))
        
        #LARGEST POSITIVE NUMBER IS SMALLEST NEGATIVE NUMBER
        res=[]
        for val,freq in (li):
            res+=[val]*freq
        return res
		
