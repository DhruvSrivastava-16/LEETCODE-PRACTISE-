class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        if len(colors) < 3:
            return False
        alice , bob = 0, 0
        i = 0
        while i < (len(colors) - 2):
            if colors[i] == colors[i+1] and colors[i] == colors[i+2]:
                if colors[i]  == "A":
                    alice+=1
                else :
                    bob+=1
            i+=1
        return alice > bob