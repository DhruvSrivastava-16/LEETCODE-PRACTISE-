class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        total = a+b+c
        A=B=C=0
        res = ""
        while total > 0:
            if (a>=b and a>=c and A!=2) or (a>0 and (B==2 or C==2)):
                res +="a"
                A+=1
                B=C=0
                a-=1
            
            elif (b>=a and b>=c and B!=2) or (b>0 and (A==2 or C==2)):
                res +="b"
                B+=1
                A=C=0
                b-=1
            
            elif (c>=b and c>=a and C!=2) or (c>0 and (B==2 or A==2)):
                res +="c"
                C+=1
                A=B=0
                c-=1
            total -=1
            
        return res