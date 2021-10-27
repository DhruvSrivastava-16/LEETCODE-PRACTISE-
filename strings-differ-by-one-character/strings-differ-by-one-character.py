class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        dict1 = {}
        m = len(dict[0])
        seen = set()
    
        for word in dict:
            for i in range(0,len(word)):
                temp = word[:i]+'.'+word[i+1:]
                if temp in seen:
                    return True
                
                seen.add(temp)
                
        return False
                