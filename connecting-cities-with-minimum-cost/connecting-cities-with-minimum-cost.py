class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n+1))
        self.ranks = [0] * (n+1)
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        """Union x and y. Return True iff union is successful
        """
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        else:
            # [optional] union with path compression
            if self.ranks[root_x] < self.ranks[root_y]:
                self.parents[root_x] = root_y
            elif self.ranks[root_x] > self.ranks[root_y]:
                self.parents[root_y] = root_x
            else:
                self.parents[root_x] = root_y
                self.ranks[root_y] += 1
            return True
    
class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        uf = UnionFind(n)
        connections.sort(key=lambda x: x[2])
        res = 0
        vertices = set()
        for root, child, wt in connections:
            if uf.union(root, child):
                res += wt
                vertices.add(root)
                vertices.add(child)
        
        # check if we have a single connected component
        if len(vertices) == n and all([uf.find(v) == uf.find(1) for v in vertices]):
            return res
        return -1