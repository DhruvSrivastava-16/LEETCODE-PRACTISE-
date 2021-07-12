class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        a = sentence.split(" ")
        for i in range(0,len(a)):
            if searchWord in a[i]:
                if searchWord[0] == a[i][0]:
                    return i+1
        
        return -1
        