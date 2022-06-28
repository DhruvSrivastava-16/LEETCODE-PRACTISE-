class Solution:
    def countDistinct(self, s: str) -> int:
        sett = set()
        for i in range(len(s)):
            for j in range(len(s),-1,-1):
                temp = s[i:j]
                sett.add(temp)
        sett.remove('')   
        return len(sett)