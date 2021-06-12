class Solution:
    def minRemoveToMakeValid(self, s: str):
        stk = []
        r= set()
        for c,i in enumerate(s):
            if i not in "()":
                continue

            if i == '(':
                stk.append(c)

            elif not stk:
                r.add(c)

            else:
                stk.pop()

        ans = ""

        r = r.union(set(stk))
        
        for i in range(0,len(s)):
            if i not in r:
                ans = ans + s[i]

        return ans