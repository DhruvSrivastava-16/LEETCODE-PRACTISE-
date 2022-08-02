class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        dic = {}
        for re in reservedSeats:
            if re[0] not in dic:
                dic[re[0]] = set()
            dic[re[0]].add(re[1])
        tot = n*2
        for key, ma in dic.items():
            a = b = c = True
            v = 0
            if 4 in ma or 5 in ma:
                a=False
                b=False
            if 6 in ma or 7 in ma:
                b=False
                c=False
            if 2 in ma or 3 in ma:
                a=False
            if 8 in ma or 9 in ma:
                c=False
            if not b:
                if not a:
                    v+=1
                if not c:
                    v+=1
            else:
                if not a:
                    v+=1
                elif not c:
                    v+=1
            tot-=v
                     
        return tot