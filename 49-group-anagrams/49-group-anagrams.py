class Solution:

            
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hmap = defaultdict(list)
        
        for st in strs:
            
            hmap[tuple(sorted(st))].append(st)
            
        return hmap.values()