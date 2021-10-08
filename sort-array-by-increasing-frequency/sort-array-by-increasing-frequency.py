from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        maps={}
        for num in nums:
            maps[num]=1+maps.get(num,0)
        mapList=sorted(maps.items(),key=lambda x:(x[1],-x[0]))
        result=[]
        for ele in mapList:
            key,value=ele
            for i in range(value):
                result.append(key)
        return result
        
        