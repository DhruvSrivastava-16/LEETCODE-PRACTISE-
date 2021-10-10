class Solution:
    
    def max_k_occurences(self,sequence,word):
        k = 1
        while word*k in sequence:
            k += 1
        return k-1


    def maxRepeating(self, sequence: str, word: str) -> int:
        return (self.max_k_occurences(sequence, word))
