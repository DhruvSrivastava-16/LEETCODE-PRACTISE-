class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a = set(edges[0])
        b = set(edges[1])
        c = a.intersection(b)
        for i in c:
            return i
            