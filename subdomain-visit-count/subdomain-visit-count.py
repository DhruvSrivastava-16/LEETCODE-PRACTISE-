class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hmap = {}
        
        for i in cpdomains:
            temp = i.split(" ")
            temp1_val = int(temp[0])
            temp2_domain = temp[1].split(".")
            
            temp3 = ""
            temp2_domain = temp2_domain[::-1]
            
            for k in temp2_domain:
                temp3 = k + temp3 
                if temp3 not in hmap:
                    hmap[temp3] = temp1_val
                    
                else:
                    hmap[temp3] = hmap[temp3] + temp1_val
                
                temp3 = '.' + temp3
                
        ans = []
        
        for k,v in hmap.items():
            temp = str(v) + " " + str(k)
            ans.append(temp)
                
        return (ans)
        