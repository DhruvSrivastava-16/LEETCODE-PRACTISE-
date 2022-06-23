from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        mapp = defaultdict(int)
        
        for domain in cpdomains:
            count, tempDomain = domain.split(' ')
            count = int(count)
            
            domainSplit = tempDomain.split('.')
        
            if len(domainSplit)==2:
                mapp[domainSplit[-1]]+=count
                mapp['.'.join(domainSplit)]+=count
                
            else:
                mapp[domainSplit[-1]]+=count
                mapp[domainSplit[-2]+'.'+domainSplit[-1]]+=count
                mapp['.'.join(domainSplit)]+=count
                
        ans = []       
        for k, v in mapp.items():
            temp = str(v)+' '+k
            ans.append(temp)
    
        return ans