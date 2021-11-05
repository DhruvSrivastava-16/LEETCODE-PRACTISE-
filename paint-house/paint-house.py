from functools import lru_cache

class Solution:
    #def minCost(self, costs: List[List[int]]) -> int:
    
   def minCost(self, costs):
    """
    :type costs: List[List[int]]
    :rtype: int
    """

    def paint_cost(n, color):
        if (n, color) in self.memo:
            return self.memo[(n, color)]
        total_cost = costs[n][color]
        if n == len(costs) - 1:
            pass
        elif color == 0:
            total_cost += min(paint_cost(n + 1, 1), paint_cost(n + 1, 2))
        elif color == 1:
            total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 2))
        else:
            total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 1))
        self.memo[(n, color)] = total_cost
        return total_cost

    if costs == []:
        return 0

    self.memo = {}
    return min(paint_cost(0, 0), paint_cost(0, 1), paint_cost(0, 2))
        