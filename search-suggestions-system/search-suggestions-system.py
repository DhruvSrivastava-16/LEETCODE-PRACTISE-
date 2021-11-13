from collections import defaultdict
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        h_map = defaultdict(list)
        
        for prod in products:
            
            temp_sr = ''
            
            for i in prod:
                temp_sr+=i
                h_map[temp_sr].append(prod)
                
        for w in h_map.values():
            w.sort()
                
        
                
        output = []
        temp = ''
        
        for ch in searchWord:
            temp+=ch
            if temp in h_map:
                if len(h_map[temp])>3:
                    output.append(h_map[temp][:3])
                    # print(output)
                else:
                    output.append(h_map[temp])

                
            else:
                output.append([])
            
            
        return output
            