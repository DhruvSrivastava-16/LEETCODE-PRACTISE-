class Solution:
    def minTimeToType(self, word: str) -> int:
        def char_dist(c1, c2):
            x = abs(ord(c1) - ord(c2))
            return min(x, 26-x)

        n = len(word)
        # edge case
        if n == 1:
            return char_dist(word[0], 'a')+1

        res = 0
        for i in range(n):
            if i == 0:
                res += char_dist(word[0], 'a')
            else:
                res += char_dist(word[i], word[i-1])

        # printing each char takes 1 second
        res += n
        
        return res