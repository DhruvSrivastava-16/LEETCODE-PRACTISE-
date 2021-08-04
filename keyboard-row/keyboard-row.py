class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = set('qwertyuiop')
        second = set("asdfghjkl")
        third = set("zxcvbnm")
        
        ans = []
        
        for w in words:
            temp = set(w.lower())
            if temp.issubset(first) or temp.issubset(second) or temp.issubset(third):
                ans.append(w)
                
        return ans
                
            