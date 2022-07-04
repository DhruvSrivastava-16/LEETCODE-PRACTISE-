class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        codeMap = defaultdict(list)
        for st in strings:
            code = ''
            for itr in range(len(st)):
                
                code+=str((ord(st[itr]) - ord(st[0])) % 26 + ord('a'))
                
            codeMap[code].append(st)
            
        return list(codeMap.values())
                
            
                
                