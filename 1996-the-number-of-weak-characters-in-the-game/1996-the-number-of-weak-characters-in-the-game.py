class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        properties.sort(key = lambda x:(x[0],-x[1]))
        ans = 0
        right = len(properties)-1
        maxDef = 0
        weak = 0
        
        while right>=0:
            
            if properties[right][1]<maxDef:
                weak+=1
                
            maxDef = max(maxDef,properties[right][1])
            right-=1
            
        return weak