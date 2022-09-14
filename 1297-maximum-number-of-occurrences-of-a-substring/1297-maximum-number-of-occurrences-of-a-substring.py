class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        s1 = []
        count ={}
        while minSize <= maxSize:
            for i in range(0,len(s)):
                if (i+ minSize) <=len(s) and len(set(s[i: i+ minSize])) <= maxLetters:
                    s1.append(s[i: i+ minSize])
            minSize += 1         
        for i in s1:
            count[i] = count[i] + 1 if i in count  else 1      
        return max(count.values()) if count else 0