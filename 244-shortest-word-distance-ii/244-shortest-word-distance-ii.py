class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.map = defaultdict(list)
        for itr in range(len(wordsDict)):
            self.map[wordsDict[itr]].append(itr)

    def shortest(self, word1: str, word2: str) -> int:
        minDiff = float('inf')
        dist1 = self.map[word1]
        dist2 = self.map[word2]
        itr1, itr2 = 0, 0
        
        while itr1<len(dist1) and itr2<len(dist2):
            
            if abs(dist1[itr1]-dist2[itr2])<minDiff:
                minDiff = abs(dist1[itr1]-dist2[itr2])
                
            if dist1[itr1]>dist2[itr2]:
                itr2+=1
                
            else:
                itr1+=1
                
        return minDiff

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)