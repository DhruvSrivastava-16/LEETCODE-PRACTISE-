class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        if len(firstList)==0 or len(secondList)==0:
            return []
        
        first_itr = 0
        second_itr = 0
        
        ans = []
        
        while (first_itr<len(firstList) and second_itr<len(secondList)):
            
            low = max(firstList[first_itr][0],secondList[second_itr][0])
            hi = min(firstList[first_itr][1],secondList[second_itr][1])
            
            if low<=hi:
                ans.append([low,hi])
            
            if secondList[second_itr][1] > firstList[first_itr][1]:
                first_itr+=1
                
            else:
                second_itr+=1
                
        return ans
                                                     
            
            
            
            
            