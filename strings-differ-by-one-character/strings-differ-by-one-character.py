class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        dict1 = {}
        m = len(dict[0])
    
        for i in dict:
            for j in range(0,m):
                temp = i[:j]+'*'+i[j+1:]
                
                if temp not in dict1:
                    dict1[temp]=1
                
                elif temp in dict1:
                    dict1[temp]+=1
                
                if dict1[temp] == 2:
                    return True
                
        return False