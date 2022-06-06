class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = []
        for i in range(len(colors)):
            for j in range(i, len(colors)):
                if i == j: continue
                if colors[i] != colors[j]:
                    ans.append(j-i)
        return max(ans)