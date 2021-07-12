class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key = lambda x: len(x))
        ans = set()
        for j in range(0,len(words)-1):
            for i in range(j+1,len(words)):
                if words[j] in words[i]:
                    ans.add(words[j])
        
        return list(ans)